import json
import time
import os
import random
from model import GPT
from prompt_loader import PromptLoader
from CodeBLEU import calc_code_bleu
from tqdm import tqdm
from utils import DataUtil, PathUtil, ModelEnum


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
        self.select = args.select
        self.name_string = PathUtil.get_name_string(self.model, self.task, self.pattern, self.task_level,
                                                    self.context_level, self.cot_level, self.source, self.temperature)
        self.loaded = self.load_model()
        if self.pattern == 'human':
            self.interactive = 1
        elif self.pattern == 'mac':
            self.interactive = 2
        elif self.pattern == 'mae':
            self.interactive = 3
        else:
            self.interactive = 0

    def load_model(self):
        if self.model == ModelEnum.GPT_3_5.value or self.model == ModelEnum.GPT_4.value:
            return GPT(self.model, self.temperature, self.max_length)

    def generate_output(self, method_name, prompts, interactive=0):
        # if len(prompt) > 2048 and self.model != ModelEnum.GPT_3_5.value:
        #     print("Prompt length exceeds the limit, truncated to 2000 characters.")
        #     prompt = prompt[:2000]
        if interactive == 0:
            output = self.loaded.run_prompts(prompts)
        elif interactive == 1:
            output = self.loaded.run_prompts_human(prompts)
        elif interactive == 2:
            output = self.loaded.run_prompts_mac(prompts)
        elif interactive == 3:
            output = self.loaded.run_prompts_mae(method_name, prompts)
        else:
            raise ValueError("Interactive mode not supported.")
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
        results = []
        for case in tqdm(self.data):
            method_idx = 0
            for method in case['methods_info']:
                method_name = method['method_name']
                tmp_prompts = []
                tmp_raw_output = []
                tmp_predicted = []
                tmp_codebleu = []
                # generate one or adapt a selected code snippet
                predicted_idx = self.select_code_snippet(method['predicted'], self.select) if 'predicted' in method else 0

                prompt_loader = PromptLoader(case, method_idx, predicted_idx, self.model, self.task, self.pattern)
                prompts = prompt_loader.generate_prompt(self.task_level, self.context_level, self.cot_level)
                # if self.model == ModelEnum.CodeGeex.value:
                #     prompt = DataUtil.convert_prompt_to_comment(prompt)
                print(f'\nAdapting the snippet at index {predicted_idx}.\n')
                for r in range(self.repeat):
                    if self.model == ModelEnum.GPT_3_5.value:
                        time.sleep(3)  # rate limit: 3 requests per minute
                    elif self.model == ModelEnum.GPT_4.value:
                        time.sleep(30)  # TO-DO: check the rate limit
                    message_history = self.generate_output(method_name, prompts, self.interactive)
                    if self.model != ModelEnum.GPT_3_5.value:
                        output = message_history
                        if r == 0:
                            try:
                                print(f'Prompt: {prompts[0]}\n')
                            except Exception as e:
                                print(e)
                    else:
                        output = message_history[-1]["content"]
                        #if r == 0:
                        for m in message_history:
                            try:
                                print(m['role'] + ":\n" + m['content'] + "\n")
                            except Exception as e:
                                print(e)
                    method_code = DataUtil.extract_method_from_output(output, method_name)
                    tmp_prompts.append('\n'.join(prompts))
                    tmp_raw_output.append(output)
                    tmp_predicted.append(method_code)
                    tmp_codebleu.append(calc_code_bleu.codebleu([DataUtil.remove_all_comments(method['solution_code'])],
                                                                [DataUtil.remove_all_comments(method_code)], 'python'))
                    method['prompt'] = tmp_prompts
                    method['raw_output'] = tmp_raw_output
                    method['predicted'] = tmp_predicted
                    method['codebleu'] = tmp_codebleu
                method_idx += 1
                self.save_tmp_results(case, case['task_id'], method_name)
            results.append(case)
        self.save_results(results)
        # self.tear_down()

    def save_results(self, res):
        output_path = PathUtil.get_output_path(self.name_string)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(res, f, indent=4)

    def save_tmp_results(self, tmp_res, tmp_idx, method_name):
        tmp_output_path = PathUtil.get_tmp_output_path(self.name_string, tmp_idx, method_name)
        with open(tmp_output_path, 'w', encoding='utf-8') as f:
            json.dump(tmp_res, f, indent=4)

    def tear_down(self):
        file_list = os.listdir("./tmp_output")
        tmp_output_prefix = f"{self.name_string}_tmp"
        for item in file_list:
            if item.startswith(tmp_output_prefix):
                os.remove(os.path.join("./tmp_output", item))
