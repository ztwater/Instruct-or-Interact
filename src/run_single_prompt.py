import json
import time
import os
import sys
import random
from model import GPT
from prompt_loader import PromptLoader
from CodeBLEU import calc_code_bleu
from tqdm import tqdm
from utils import DataUtil, PathUtil, ModelEnum, TaskEnum
from func_timeout import func_set_timeout
from func_timeout.exceptions import FunctionTimedOut
import importlib
import unittest
from test import Test


class Inference:
    def __init__(self, args):
        self.data = DataUtil.load_data(args.data_path, args.start_idx, args.end_idx)
        self.model = args.model
        self.temperature = args.temperature
        self.max_length = args.max_length
        self.task = args.task
        self.pattern = args.pattern
        self.task_level = args.task_level
        self.context_level = args.context_level
        self.cot_level = args.cot_level
        self.repeat = args.repeat
        self.load_from_local = args.load_from_local
        self.cuda = args.cuda
        self.source = args.source
        if self.source == 'human':
            with open('../data/random_list_200.json', 'r', encoding='utf-8') as f:
                self.random_list = json.load(f)
        self.select = args.select
        self.name_string = PathUtil.get_name_string(self.model, self.task, self.pattern, self.task_level,
                                                    self.context_level, self.cot_level, self.source, self.temperature)
        self.loaded = self.load_model()
        self.is_interactive = True if self.pattern == 'interactive' else False
        self.test = Test(args)
        self.test_names = DataUtil.get_test_names()

    def load_model(self):
        if self.model == ModelEnum.GPT_3_5.value or self.model == ModelEnum.GPT_4.value:
            return GPT(self.model, self.temperature, self.max_length)

    def generate_output(self, prompts, interactive=False):
        if interactive:
            output = self.loaded.run_prompts_human(prompts)
        else:
            output = self.loaded.run_prompts(prompts)
        return output

    @staticmethod
    def select_code_snippet(code_list, mode):
        if mode == 'random':
            random.seed(0)
            return random.randint(0, len(code_list) - 1)
        elif mode == 'test':
            return 0
        elif mode == 'codebleu':
            return 0
        elif mode == 'codebertscore':
            return 0
        pass

    def pipeline(self):
        for case in tqdm(self.data):
            method_idx = 0
            task_id = case['task_id']
            for method in case['methods_info']:
                method_name = method['method_name']
                if not self.is_selected_method(task_id, method_name):
                    method_idx += 1
                    continue
                tmp_prompts = []
                tmp_questions = []
                tmp_answers = []
                tmp_raw_output = []
                tmp_predicted = []
                tmp_codebleu = []
                # test_code = "import unittest\n\n"
                test_code = '\n'.join(DataUtil.extract_imports(case['test'])) + '\n\n'
                test_code += method['test_code']
                test_class_name = method['test_class']
                method_test_names = self.test_names[task_id][method_name]
                test_results_method = {}
                # generate one or adapt a selected code snippet
                predicted_idx = self.select_code_snippet(method['predicted'], self.select) if 'predicted' in method else 0
                prompt_loader = PromptLoader(case, method_idx, predicted_idx, self.model, self.task, self.pattern)
                prompts = prompt_loader.generate_prompt(self.task_level, self.context_level, self.cot_level)
                print(f'\nAdapting the snippet at index {predicted_idx}.\n')
                for r in range(self.repeat):
                    if r == 0:
                        try:
                            prompts_str = '\n'.join(prompts)
                            print(f"Prompt:\n{prompts_str}\n")
                        except Exception as e:
                            print(e)
                    message_history = self.generate_output(prompts, self.is_interactive)
                    output = message_history[-1]["content"]
                    try:
                        print(output)
                    except Exception as e:
                        print(e)
                    method_code = DataUtil.extract_method_from_output(output, method_name)
                    tmp_prompts.append('\n'.join(prompts))
                    tmp_raw_output.append(output)
                    tmp_predicted.append(method_code)
                    tmp_codebleu.append(calc_code_bleu.codebleu([method['solution_code']], [method_code], 'python'))
                    q, a = self.parse_message_history(message_history, len(prompts))
                    tmp_questions.append('\n'.join(q))
                    tmp_answers.append('\n'.join(a))

                    # write .py files for unit test
                    predicted_code = DataUtil.replace_method_in_code(case['solution_code'], method_name, method_code)
                    test_code_py = predicted_code + "\n\n" + test_code
                    with open(os.path.join(PathUtil.get_tmp_test_file_output_path(),
                                           f"{task_id}_{method_name}_{str(r)}.py"), 'w', encoding='utf-8') as f:
                        f.write(test_code_py)
                    # run unit tests
                    tmp_test_results = self.get_unit_test_results(task_id, method_name, test_class_name, r)
                    print("========== Tmp Test Results ==========")
                    print("Test results for the current generated method: " + str(tmp_test_results))
                    print("======================================")
                    iteration_name = method_name + '_' + str(r)
                    test_results_method[iteration_name] = tmp_test_results

                method['prompt'] = tmp_prompts
                method['raw_output'] = tmp_raw_output
                method['predicted'] = tmp_predicted
                method['codebleu'] = tmp_codebleu
                method['questions'] = tmp_questions
                method['answers'] = tmp_answers
                method['test_result'] = test_results_method
                self.save_tmp_results(case, task_id, method_name)
                pass_at_1, overview, errors = self.evaluate_test_results(test_results_method, method_test_names, 1)
                pass_at_5, _, _ = self.evaluate_test_results(test_results_method, method_test_names,5)
                print("========== Method Test Results ==========")
                print("avg_codebleu: ", sum(method['codebleu']) / len(method['codebleu']))
                print("pass@1: ", pass_at_1)
                print("pass@5: ", pass_at_5)
                print("overview: ", overview)
                print("errors: ", errors)
                print("=========================================")
                method_idx += 1

    def parse_message_history(self, message_history, turns):
        questions = [m['content'] for m in message_history[2*turns::2]]
        try:
            answers = [m['content'] for m in message_history[2*turns+1::2]]
        except Exception as e:
            answers = []
        return questions, answers

    def is_selected_method(self, task_id, method_name):
        for d in self.random_list:
            if d['method_name'] == method_name and d['task_id'] == task_id:
                return True
        return False

    def get_unit_test_results(self, task_id, method_name, test_class_name, iteration):
        print(f"testing {task_id} {method_name} {iteration}")
        test_module_name = task_id + '_' + method_name + '_' + str(iteration)
        iteration_name = method_name + '_' + str(iteration)
        res_item = {}
        try:
            res = self.test.run_unit_test(test_module_name, test_class_name)
            res_item['compilation'] = 'success'
            res_item['errors'] = self.test.get_error_log(res.errors)
            res_item['failures'] = self.test.get_error_log(res.failures)
            res_item['total_run'] = res.testsRun
        except Exception as e:
            print(e)
            res_item['compilation'] = str(e)
            res_item['errors'] = {}
            res_item['failures'] = {}
            res_item['total_run'] = 0
        # catch the timeout exception
        except FunctionTimedOut as timeout:
            print(timeout)
            res_item['compilation'] = 'success'
            res_item['errors'] = {'TimeoutError': {}}
            res_item['failures'] = {}
            res_item['total_run'] = 0
        return res_item

    def evaluate_test_results(self, test_results_method, method_test_names, k):
        overview = {'num_fail': 0, 'num_partial': 0, 'num_pass': 0, 'num_total': 0}
        errors = {}
        total_tmp = len(test_results_method)
        method_test_results = self.test.evaluate_method_test_outputs(test_results_method, method_test_names)
        pass_tmp = method_test_results['Success']
        overview['num_total'] += total_tmp
        overview['num_pass'] += method_test_results['Success']
        overview['num_partial'] += method_test_results['Partial']
        overview['num_fail'] += method_test_results['Failed']
        errors['Error'] = method_test_results['Error']
        errors['Failure'] = method_test_results['Failure']
        errors['TimeoutError'] = method_test_results['TimeoutError']
        errors['CompilationError'] = method_test_results['CompilationError']
        pass_at_k = self.test.pass_at_k(total_tmp, pass_tmp, k)  # if total_tmp != 0 else 0
        return pass_at_k, overview, errors

    def save_tmp_results(self, tmp_res, tmp_idx, method_name):
        tmp_output_path = PathUtil.get_tmp_output_path(self.name_string, tmp_idx, method_name)
        with open(tmp_output_path, 'w', encoding='utf-8') as f:
            json.dump(tmp_res, f, indent=4)
