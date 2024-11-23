import pandas as pd
from func_timeout import func_set_timeout
from func_timeout.exceptions import FunctionTimedOut
import importlib
import unittest
import os
import json
import sys
import numpy as np
import shutil
from scipy.special import comb
from utils import PathUtil, DataUtil
from CodeBLEU import calc_code_bleu
import argparse


class Test:
    def __init__(self, args):
        self.model = args.model
        self.task = args.task
        self.pattern = args.pattern
        self.task_level = args.task_level
        self.context_level = args.context_level
        self.cot_level = args.cot_level
        self.source = args.source
        # for manual annotated 200 cases
        if self.source == 'manual':
            with open('../data/random_list_200.json', 'r', encoding='utf-8') as f:
                self.random_list = json.load(f)
        self.temperature = args.temperature
        self.name_string = PathUtil.get_name_string(self.model, self.task, self.pattern, self.task_level,
                                                    self.context_level, self.cot_level, self.source, self.temperature)

    def get_output_data(self):
        output_path = PathUtil.get_output_path(self.name_string)
        return DataUtil.load_data_as_dict(output_path)

    @func_set_timeout(5)  # set timeout to 5 seconds
    def run_unit_test(self, module_name, class_name):
        tmp_test_file_output_path = PathUtil.get_tmp_test_file_output_path()
        sys.path.append(tmp_test_file_output_path)
        test_module = importlib.import_module(module_name)  # dynamically import the module specified by module_name
        test_class = getattr(test_module, class_name)
        log_path = PathUtil().get_log_output_path(self.name_string)
        with open(log_path, 'a', encoding='utf-8') as f:
            os.chdir(tmp_test_file_output_path)
            # load the test cases from the test method specified by test_method in the dynamically imported module
            test_suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
            # runs the loaded test suite and write the test result to the log file
            test_result = unittest.TextTestRunner(stream=f).run(test_suite)
            os.chdir(os.path.abspath(os.path.dirname(__file__)))
        return test_result

    def get_unit_test_results(self, test_num, task_id, method_name, test_class_name):
        unit_test_results = {}
        for i in range(test_num):
            print(f"testing {task_id} {method_name} {i}")
            test_module_name = task_id + '_' + method_name + '_' + str(i)
            iteration_name = method_name + '_' + str(i)
            res_item = {}
            try:
                res = self.run_unit_test(test_module_name, test_class_name)
                res_item['compilation'] = 'success'
                res_item['errors'] = self.get_error_log(res.errors)
                res_item['failures'] = self.get_error_log(res.failures)
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
            unit_test_results[iteration_name] = res_item
        return unit_test_results

    def pipeline(self):
        data = self.get_output_data()
        # update codebleu if no code codebleu values
        # data = self.add_codebleu(data)
        # output_path = PathUtil.get_output_path(self.name_string)
        # with open(output_path, 'w', encoding='utf-8') as f:
        #     json.dump(data, f, indent=4)
        # data = self.get_output_data()

        # calculate average codebleu
        codebleu_list = []
        for task_id in data:
            for method in data[task_id]['methods_info']:
                if self.source == 'manual':
                    if self.is_selected_method(task_id, method['method_name']):
                        codebleu_list.extend(method['codebleu'])
                else:
                    try:
                        codebleu_list.extend(method['codebleu'])
                    except KeyError:
                        print(f"CodeBLEU not found for {task_id} {method['method_name']}")
        print("Average CodeBLEU: ", sum(codebleu_list) / len(codebleu_list))

        # get the predicted code list
        predicted_code_list = DataUtil.synthesize_predicted_code(data)

        # get test code and generate py file for each method
        for task_id in predicted_code_list:
            for method_name in predicted_code_list[task_id]:
                if self.source == 'manual' and not self.is_selected_method(task_id, method_name):
                    continue
                # get method index in the original data
                method_index = DataUtil.get_method_index(data[task_id], method_name)
                if method_index != -1:
                    # test_code = "import unittest\n\n"
                    test_code = '\n'.join(DataUtil.extract_imports(data[task_id]['test'])) + '\n\n'
                    test_code += data[task_id]['methods_info'][method_index]['test_code']
                    cnt = 0
                    # write .py files for test
                    for predicted_code in predicted_code_list[task_id][method_name]:
                        test_code_py = predicted_code + "\n\n" + test_code
                        with open(os.path.join(PathUtil.get_tmp_test_file_output_path(),
                                               f"{task_id}_{method_name}_{str(cnt)}.py"), 'w', encoding='utf-8') as f:
                            f.write(test_code_py)
                        cnt += 1
                else:
                    raise Exception(f"Method name {method_name} not found in {task_id}")

        # run unit tests
        test_results = {}
        for task_id in predicted_code_list:
            test_results[task_id] = {}
            for method_name in predicted_code_list[task_id]:
                if self.source == 'manual' and not self.is_selected_method(task_id, method_name):
                    continue
                method_index = DataUtil.get_method_index(data[task_id], method_name)
                if method_index != -1:
                    test_num = len(predicted_code_list[task_id][method_name])
                    test_class_name = data[task_id]['methods_info'][method_index]['test_class']
                    test_results[task_id][method_name] = self.get_unit_test_results(test_num, task_id, method_name, test_class_name)
                else:
                    raise Exception(f"Method name {method_name} not found in {task_id}")
        # print(test_results)
        # self.tear_down()
        return test_results

    def is_selected_method(self, task_id, method_name):
        for d in self.random_list:
            if d['method_name'] == method_name and d['task_id'] == task_id:
                return True
        return False

    def save_results(self, res):
        test_output_path = PathUtil.get_test_output_path(self.name_string)
        with open(test_output_path, 'w', encoding='utf-8') as f:
            json.dump(res, f, sort_keys=True, indent=4)

    @staticmethod
    def tear_down():
        tmp_test_path = PathUtil.get_tmp_test_file_output_path()
        file_list = os.listdir(tmp_test_path)
        for item in file_list:
            file_path = os.path.join(tmp_test_path, item)
            if "__pycache__" not in file_path:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)

    @staticmethod
    def get_error_log(failed_tests):
        error_dict = {}
        for failed_test in failed_tests:
            test_id, stacktrace = failed_test
            current_test_name = str(test_id).split(' ')[0]
            stacks = stacktrace.split('\n')
            error_output = ''
            for stack in stacks:
                # get the line with 'XXXError:'
                if 'Error:' in stack:
                    error_output = stack
                    break
            # error_output = stacktrace.split('\n')[-2]  # get the last line of the stacktrace
            error_type, error_info = error_output.split('Error:')
            error_type += 'Error'
            error_info = error_info.strip()
            if error_type not in error_dict:
                error_dict[error_type] = {}
            error_dict[error_type][current_test_name] = error_info
        return error_dict

    @staticmethod
    def evaluate_single_method_test(result_dict):
        error_cnt = {}
        error_num = sum([len(v) for _, v in result_dict['errors'].items()])
        failure_num = sum([len(v) for _, v in result_dict['failures'].items()])
        # print(error_num, failure_num, result_dict['total_run'])
        if result_dict['total_run'] == 0:
            single_test_result = -1
            if result_dict['compilation'] != 'success':
                error_cnt['CompilationError'] = 1
            else:
                error_cnt['TimeoutError'] = 1
        elif error_num + failure_num == 0:  # success
            single_test_result = 1
        else:
            for error_type in result_dict['errors']:
                error_cnt[error_type] = len(result_dict['errors'][error_type])
            for error_type in result_dict['failures']:
                error_cnt[error_type] = len(result_dict['failures'][error_type])
            if error_num + failure_num < result_dict['total_run']:
                single_test_result = 0
            else:
                single_test_result = -1
        return single_test_result, error_cnt

    @staticmethod
    def evaluate_method_test_outputs(result_dict, test_names):
        results = {}
        results['Success'] = 0
        results['Partial'] = 0
        results['Failed'] = 0
        results['TimeoutError'] = 0
        results['CompilationError'] = 0
        results['Error'] = 0
        results['Failure'] = 0
        results['Passed'] = 0
        results['Tests'] = {}
        for test_name in test_names:
            results['Tests'][test_name] = {}
        for _, single_result in result_dict.items():
            error_num = sum([len(v) for _, v in single_result['errors'].items()])
            failure_num = sum([len(v) for _, v in single_result['failures'].items()])
            if single_result['total_run'] == 0:
                if single_result['compilation'] != 'success':
                    results['CompilationError'] += 1
                    for test_name in test_names:
                        results['Tests'][test_name].setdefault('CompilationError', 0)
                        results['Tests'][test_name]['CompilationError'] += 1
                else:
                    results['TimeoutError'] += 1
                    for test_name in test_names:
                        results['Tests'][test_name].setdefault('TimeoutError', 0)
                        results['Tests'][test_name]['TimeoutError'] += 1
            else:
                results['Error'] += error_num
                results['Failure'] += failure_num
                passed = {}
                for test_name in test_names:
                    passed[test_name] = True
                if error_num + failure_num == 0:  # success
                    results['Success'] += 1
                else:  # failed tests
                    for error_type in single_result['errors']:
                        for error_test_name in single_result['errors'][error_type]:
                            results['Tests'][error_test_name].setdefault(error_type, 0)
                            results['Tests'][error_test_name][error_type] += 1
                            passed[error_test_name] = False
                    for error_type in single_result['failures']:
                        for error_test_name in single_result['failures'][error_type]:
                            results['Tests'][error_test_name].setdefault(error_type, 0)
                            results['Tests'][error_test_name][error_type] += 1
                            passed[error_test_name] = False
                    if sum(passed.values()) > 0:
                        results['Partial'] += 1
                    else:
                        results['Failed'] += 1
                results['Passed'] += sum(passed.values())
        return results

    def evaluate_test_results(self, test_results, k):
        pass_at_k_list = []
        test_names = DataUtil.get_test_names()
        pass_at_k = 0
        overview = {'num_fail': 0, 'num_partial': 0, 'num_pass': 0, 'num_total': 0}
        errors = {}
        method_num = 0
        for task_id in test_results:
            for method_name in test_results[task_id]:
                total_tmp = len(test_results[task_id][method_name])
                method_test_names = test_names[task_id][method_name]
                method_test_results = self.evaluate_method_test_outputs(test_results[task_id][method_name], method_test_names)
                pass_tmp = method_test_results['Success']
                overview['num_total'] += total_tmp
                overview['num_pass'] += method_test_results['Success']
                overview['num_partial'] += method_test_results['Partial']
                overview['num_fail'] += method_test_results['Failed']
                errors['Error'] = method_test_results['Error']
                errors['Failure'] = method_test_results['Failure']
                errors['TimeoutError'] = method_test_results['TimeoutError']
                errors['CompilationError'] = method_test_results['CompilationError']
                pass_at_k_tmp = self.pass_at_k(total_tmp, pass_tmp, k)  # if total_tmp != 0 else 0
                pass_at_k_list.append([method_name, pass_at_k_tmp])
                pass_at_k += pass_at_k_tmp
                method_num += 1
        pass_at_k = pass_at_k / method_num
        pass_at_k_df = pd.DataFrame(pass_at_k_list, columns=['method_name', f'pass_at_{k}'])
        with open(PathUtil.get_test_output_path(self.name_string) + f'_pass_at_{k}.csv', 'w', encoding='utf-8') as f:
            pass_at_k_df.to_csv(f, index=False)
        return pass_at_k, overview, errors

    @staticmethod
    def pass_at_k(n, c, k):
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

    @staticmethod
    def pass_at_k_classeval(n, c, k):
        total_combinations = comb(n, k)
        if n - c >= k:
            without_pass_combinations = comb(n - c, k)
        else:
            without_pass_combinations = 0
        with_pass_combinations = total_combinations - without_pass_combinations
        pass_at_k = with_pass_combinations / total_combinations
        return pass_at_k

    def add_codebleu(self, output_data):
        lang = 'python'
        params = (0.25, 0.25, 0.25, 0.25)
        for task_id in output_data:
            for method in output_data[task_id]['methods_info']:
                method_name = method['method_name']
                if self.source == 'manual' and not self.is_selected_method(task_id, method_name):
                    continue
                predicted = [DataUtil.remove_all_comments(m) for m in method['predicted']]
                solution = DataUtil.remove_all_comments(method['solution_code'])
                res = []
                for p in predicted:
                    res.append(calc_code_bleu.codebleu([solution], [p], lang, params))
                method['codebleu'] = res
        keys = sorted(map(lambda x: int(x[10:]), output_data.keys()))
        output_data = [output_data['ClassEval_' + str(k)] for k in keys]
        return output_data

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        type=int,
        default=0,
        help="model name, default is 0 ('gpt-3.5-turbo')"
    )
    parser.add_argument(
        "--task",
        type=int,
        default=0,
        help="task type, default is 0 (method generation)"
    )
    parser.add_argument(
        "--pattern",
        type=str,
        default="direct",
        help="prompt pattern"
    )
    parser.add_argument(
        "--task_level",
        type=int,
        default=0,
        help="task level, default is 0 (simple task description)"
    )
    parser.add_argument(
        "--context_level",
        type=int,
        default=0,
        help="context level, default is 0 (no context)"
    )
    parser.add_argument(
        "--cot_level",
        type=int,
        default=0,
        help="CoT level, default is 0 (no steps)"
    )
    parser.add_argument(
        "--source",
        type=str,
        default='',
        help="adaptation source, default is None"
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.2,
        help="temperature value in generation config"
    )
    args = parser.parse_args()
    test = Test(args)
    test_results = test.pipeline()
    test.save_results(test_results)

    pass_at_1, overview, errors = test.evaluate_test_results(test_results, 1)
    pass_at_5, _, _ = test.evaluate_test_results(test_results, 5)
    print("pass@1:", pass_at_1)
    print("pass@5:", pass_at_5)
    print("overview:", overview)
    print("errors:", errors)
