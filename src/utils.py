import re
from enum import Enum
import json
import os
from typing import List, Dict, Tuple, Union


class PromptUtils:

    # ==================== Prompt Style ====================
    @staticmethod
    def pattern_instruction_style(instruction):
        return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:\n"""

    @staticmethod
    def pattern_direct_style(instruction):
        return instruction

    # ==================== Task Description ====================
    @staticmethod
    def method_generation_task(method_name, method_description, class_name, task_level):
        method_signature = DataUtil.extract_method_signature(method_name, method_description)
        method_desc_dict = DataUtil.parse_method_description(method_name, method_description)
        method_function = method_desc_dict['function']
        if task_level == 0:  # name + function
            return f"Please write a Python method `{method_name}` to complete the function: {method_function}."
        elif task_level == 1:  # name + signature + function
            return f"Please write a Python method `{method_name}` to complete the function: {method_function}, " \
                   f"whose signature should be `{method_signature}`."
        elif task_level == 2:  # name + class context (where signature and function are described)
            return f"Please complete `{method_name}` method in the following class `{class_name}`."
        elif task_level == 3:  # name + NL description (i.e. task_level=2 and context_level=0)
            task_prompt = f"Please complete `{method_name}` method in the following class `{class_name}`.\n"
            task_prompt += PromptUtils.construct_nl_method_description(method_desc_dict)
            task_prompt += "Then write out method completely in the Response section."
            return task_prompt
        else:
            raise Exception("task level is not supported")

    @staticmethod
    def method_generation_task_cc(method_name, method_description, class_name, task_level):
        method_signature = DataUtil.extract_method_signature(method_name, method_description)
        method_desc_dict = DataUtil.parse_method_description(method_name, method_description)
        method_function = method_desc_dict['function']
        if task_level == 0:  # name + function
            return f"    # {method_function}\n    def {method_name}("
        elif task_level == 1:  # signature + function above
            return f"    # {method_function}\n    {method_signature}\n"
        elif task_level == 2:  # signature + function as docstring
            return f"    {method_signature}\n        \"\"\"\n        {method_desc_dict['function']}\n        \"\"\"\n"
        else:
            raise Exception("task level is not supported")

    @staticmethod
    def adaptation_task(method_name, method_description, class_name, task_level):
        method_desc_dict = DataUtil.parse_method_description(method_name, method_description)
        task_prompt = ''
        if task_level == 0:  # name + method description in the code format
            task_prompt += f"Please adapt the provided method `{method_name}` to the class context of `{class_name}`.\n" \
                            "The adapted method should perform the function in the following description:\n" \
                           f"```\n    {method_description}\n```\n"
        elif task_level == 1:  # name + NL description
            task_prompt += PromptUtils.construct_nl_method_description(method_desc_dict)
        elif task_level == 2:  # interactive task prompt
            task_prompt += (f"I would like you to ask me at most 3 questions to retrieve necessary information to "
                            f"adapt the above provided code snippet `{method_name}` to the class context of "
                            f"`{class_name}`. The adapted method should perform the function in the following "
                            f"description:\n```\n    {method_description}\n```\n")
        else:
            raise Exception("Task level is not supported.")
        return task_prompt

    @staticmethod
    def construct_nl_method_description(method_desc_dict):
        prompt = ""
        if method_desc_dict['function'] != '':
            prompt += f"This method should implement the function: {method_desc_dict['function']}."
        if method_desc_dict['parameters'] != '':
            prompt += f"The method should take the following parameters:\n```\n{method_desc_dict['parameters']}\n```\n"
        else:
            prompt += "The method should take no parameters.\n"
        if method_desc_dict['return'] != '':
            prompt += f"The method should return: '{method_desc_dict['return']}'\n"
        else:
            prompt += "The method should return no value.\n"
        if method_desc_dict['inputs'] != '':
            prompt += f"For the following example input(s):\n```\n{method_desc_dict['inputs']}\n```\n"
        if method_desc_dict['outputs'] != '':
            prompt += f"The method should obtain the following example output(s):\n" \
                      f"```\n{method_desc_dict['outputs']}\n```\n"
        return prompt

    @staticmethod
    def class_context_classeval(import_statement, class_constructor, class_description):
        class_context = '\n'.join(import_statement)
        class_context_list = class_constructor.split('\n')
        class_context_list[0] += " \n" + class_description
        class_context += '\n' + '\n'.join(class_context_list)
        return class_context

    # ==================== Role Description ====================
    @staticmethod
    def role_description(role_desc='assistant'):
        if role_desc == 'assistant':
            return "You are a helpful assistant."
        else:
            return role_desc

    # ==================== Chain-of-Thoughts Description ====================
    @staticmethod
    def generation_step(cot_level, restriction_dependencies):
        if cot_level == 0:
            return "Please write out the generated method completely in the Response section.\n"
        elif cot_level == 1:
            return "Please write out the generated method completely in the Response section. " + restriction_dependencies + "\n"
        else:
            raise Exception("CoT level is not supported.")

    @staticmethod
    def adaptation_step(cot_level, restriction_dependencies):
        if cot_level == 0:
            return "Please write out the adapted method completely in the Response section.\n"
        elif cot_level == 1:  # provide dependencies
            return "Please write out the adapted method completely in the Adapted Method section. " + restriction_dependencies + "\n"
        elif cot_level == 2:  # interactive
            return restriction_dependencies + '\n' + "Once you have sufficient information, please write out the adapted method.\n"

    @staticmethod
    def restriction_dependencies(dep_dict: Dict[str, str]) -> str:
        """
        Restrict LLMs to generate code using certain dependencies.
        :param dep_dict: Dict[str, str], the dependency dict of a method
        :return: a candidate description to describe dependencies in the prompt
        """
        if dep_dict['Standalone']:
            return "It should be implemented without using any external libraries, member variables or methods."
        lib_dep = 'libraries: ' + ', '.join(['`' + dep + '`' for dep in dep_dict['lib_dependencies']]) if len(dep_dict['lib_dependencies']) > 0 else None
        field_dep = 'fields: ' + ', '.join(['`' + dep + '`' for dep in dep_dict['field_dependencies']]) if len(dep_dict['field_dependencies']) > 0 else None
        method_dep = 'methods: ' + ', '.join(['`' + dep + '`' for dep in dep_dict['method_dependencies']]) if len(dep_dict['method_dependencies']) > 0 else None
        return f"It should be implemented using {', '.join([x for x in [lib_dep, field_dep, method_dep] if x is not None])}."


class DataUtil:
    @staticmethod
    def load_data(data_path, start_idx, end_idx):
        with open(data_path, encoding='utf-8') as file:
            data_json = json.load(file)
        return data_json[start_idx:end_idx]

    @staticmethod
    def load_data_as_dict(data_path):
        data = {}
        with open(data_path, encoding='utf-8') as file:
            data_json = json.load(file)
        for item in data_json:
            data[item['task_id']] = item
        return data

    @staticmethod
    def get_leading_spaces(string):
        return len(string) - len(string.lstrip())

    @staticmethod
    def extract_imports(code):
        """
        Extract the import statements from the code.
        """
        import_list = []
        lines = code.split('\n')
        for line in lines:
            if line.startswith('import') or line.startswith('from'):
                import_list.append(line)
        return import_list

    @staticmethod
    def extract_method_name(code):
        """
        Extract the method name from a method code, considering the scenario that the generated or retrieved method
        code has the different name from the target method.
        """
        first_line = code.split('\n')[0]
        if 'def' in first_line:
            return first_line.split('def ')[1].split('(')[0]
        return ""

    @staticmethod
    def extract_method_signature(method_name, method_description):
        """
        Extract the method signature from the method description.
        """
        desc_list = method_description.split('\n')
        for line in desc_list:
            method_def_prefix = "def " + method_name + '('
            if method_def_prefix in line:
                return line.lstrip()
        # if method signature not found
        raise Exception(f"Method signature for {method_name} not found.")

    @staticmethod
    def extract_all_comments(text):
        """
        Extract all the text between \"\"\" and \"\"\"
        :param text: str
        :return: List[str]
        """
        comments = []
        lines = text.split('\n')
        is_comment = False
        for line in lines:
            if '\"\"\"' in line:
                is_comment = not is_comment
                continue
            if is_comment and line.strip() != '':
                comments.append(line.strip())
        return comments

    @staticmethod
    def remove_inline_comments(line):
        result = []
        in_single_quote = False
        in_double_quote = False

        for char_index, char in enumerate(line):
            if char == "#" and not in_single_quote and not in_double_quote:
                break  # Stop when a '#' is found outside of quotes
            elif char == "'":
                in_single_quote = not in_single_quote
            elif char == '"':
                in_double_quote = not in_double_quote
            result.append(char)

        return "".join(result)

    @staticmethod
    def remove_all_comments(code):
        multiline_comment_pattern = r'(?<=:\n\s{8})(\'\'\'(.*?)\'\'\'|\"\"\"(.*?)\"\"\")'
        # remove multiline comments
        method_code = re.sub(multiline_comment_pattern, '', code, flags=re.DOTALL)
        # split the code into lines
        lines = method_code.split('\n')
        new_lines = []
        for line in lines:
            new_lines.append(DataUtil.remove_inline_comments(line))
        # remove empty lines
        new_lines = [line for line in new_lines if line.strip() != '']
        return '\n'.join(new_lines)

    @staticmethod
    def parse_method_description(method_name, method_description):
        """
        Extract method function, parameter description, return description and
        example input/output from method description.
        """
        method_dict = {}
        method_dict['signature'] = DataUtil.extract_method_signature(method_name, method_description)
        comments = DataUtil.extract_all_comments(method_description)

        param_list = []
        input_list = []
        output_list = []
        param_line = -1
        return_line = -1
        input_line = -1
        output_line = -1
        idx = 0
        for c in comments:
            param_index = c.find(':param')
            return_index = c.find(':return')
            input_index = c.find('>>>')
            if param_index != -1:
                param_list.append(c[param_index + len(':param'):].lstrip())
                param_line = idx if param_line == -1 else param_line
            if return_index != -1:
                tmp_return = c[return_index + len(':return'):].lstrip()
                # remove the colons and spaces in the beginning
                tmp_return = tmp_return.lstrip(':').lstrip()
                method_dict['return'] = tmp_return
                return_line = idx if return_line == -1 else return_line
            if input_index != -1:
                input_list.append(c[input_index + len('>>>'):].lstrip())
                input_line = idx if input_line == -1 else input_line
                output_line = idx + 1
            elif output_line != -1:
                output_list.append(c.strip())
            idx += 1
        cmp = [param_line, return_line, input_line, output_line]
        cmp = [c for c in cmp if c != -1]
        func_line = min(cmp) if len(cmp) > 0 else -1
        tmp_func = ' '.join(comments[:func_line])
        # replace newlines with spaces
        method_dict['function'] = tmp_func.replace('\n', ' ')
        method_dict['parameters'] = '\n'.join(param_list)
        if 'return' not in method_dict:
            method_dict['return'] = ''
        method_dict['inputs'] = '\n'.join(input_list)
        method_dict['outputs'] = '\n'.join(output_list)
        return method_dict

    @staticmethod
    def get_method_index(task, method_name):
        for i in range(len(task['methods_info'])):
            if task['methods_info'][i]['method_name'] == method_name:
                return i
        return -1

    @staticmethod
    def is_dependent(method1, method2):
        d1 = method1['dependencies']['method_dependencies']
        d2 = method2['dependencies']['method_dependencies']
        # exchange the two comparisons to avoid wrong label
        if method1['method_name'] in d2:
            return -1
        elif method2['method_name'] in d1:
            return 1
        else:
            return 0

    @staticmethod
    def extract_method_from_output(output, method_name):
        """
        extract the method code from LLM output
        """
        # handle different heads of the output
        if "### Response:" in output:
            code_list = output.split("### Response:")[1].split('\n')
        else:
            code_list = output.split('\n')
        # prune the code with too many rows such as infinitely generated '# ...\n' by GPT-3.5
        if len(code_list) > 100:
            code_list = code_list[:100]
        method_code_list = []
        is_this_method = False
        method_def_prefix = "def " + method_name + '('
        leading_space = 0
        first_cont_line_space = -1
        for i, line in enumerate(code_list):
            if method_def_prefix in line:
                is_this_method = True
                leading_space = DataUtil.get_leading_spaces(line)
                if leading_space >= 4:
                    cut_space = leading_space - 4
                    method_code_list.append(line[cut_space:])
                else:
                    method_code_list.append(' ' * (4 - leading_space) + line)
            elif is_this_method:
                if DataUtil.get_leading_spaces(line) > leading_space or len(line) == 0 or all(char.isspace() for char in line):
                    if first_cont_line_space == -1 and len(line) != 0 and not all(char.isspace() for char in line):
                        first_cont_line_space = DataUtil.get_leading_spaces(line)
                    if first_cont_line_space >= 8:
                        _cut_space = first_cont_line_space - 8
                        method_code_list.append(line[_cut_space:])
                    else:
                        method_code_list.append(' ' * (8 - first_cont_line_space) + line)
                else:
                    break
        method_code = '\n'.join(method_code_list)
        return method_code

    @staticmethod
    def replace_method_in_code(code, method_name, method_code):
        """
        replace the method code in the class code
        """
        code_list = code.split('\n')
        method_code_list = method_code.split('\n')
        target_code_list = []
        method_def_prefix = "def " + method_name + '('
        leading_space = 0
        is_this_method = False
        for line in code_list:
            if method_def_prefix in line:
                is_this_method = True
                leading_space = DataUtil.get_leading_spaces(line)
            elif is_this_method:
                if DataUtil.get_leading_spaces(line) > leading_space or len(line) == 0 or line == '\r':
                    continue
                else:
                    is_this_method = False
                    for method_line in method_code_list:
                        target_code_list.append(method_line)
                    target_code_list.append('')  # add a blank line before next method
                    target_code_list.append(line)
            else:
                target_code_list.append(line)
        # replace the last method
        if is_this_method:
            for method_line in method_code_list:
                target_code_list.append(method_line)
        return '\n'.join(target_code_list)

    @staticmethod
    def synthesize_predicted_code(model_output):
        """
        get predicted methods from the output file and synthesize them into the class code
        """
        predicted_code_list = {}
        for task_id in model_output:
            solution_code = model_output[task_id]['solution_code']
            predicted_code_list[task_id] = {}
            for method in model_output[task_id]['methods_info']:
                method_name = method['method_name']
                predicted_code_list[task_id][method_name] = []
                if 'predicted' not in method:
                    continue
                for m in method['predicted']:
                    predicted_code = DataUtil.replace_method_in_code(solution_code, method_name, m)
                    predicted_code_list[task_id][method_name].append(predicted_code)
        return predicted_code_list

    @staticmethod
    def convert_prompt_to_comment(prompt):
        """
        For codegeex2, prompts should be written as comments
        """
        head = '# language: Python\n'
        lines = ['# ' + line for line in prompt.split('\n')]
        lines = [head] + lines
        return '\n'.join(lines)

    @staticmethod
    def save_ref_and_hyps(ref, hyps, code_output_dir):
        ref_path = os.path.join(code_output_dir, 'ref.py')
        with open(ref_path, 'w', encoding='utf-8') as f:
            f.write(ref)
        for h in range(len(hyps)):
            hyp_path = os.path.join(code_output_dir, f'hyp_{h}.py')
            with open(hyp_path, 'w', encoding='utf-8') as f:
                f.write(hyps[h])

    @staticmethod
    def get_test_names():
        data = DataUtil.load_data(PathUtil.get_data_path(), 0, 100)
        test_names = {}
        for i in range(100):
            task_id = 'ClassEval_' + str(i)
            test_names[task_id] = {}
            for method in data[i]['methods_info']:
                test_code = method['test_code']
                test_codeline = test_code.split('\n')
                # extract all test method names for test_codeline
                test_names[task_id][method['method_name']] = []
                for line in test_codeline:
                    line = line.strip()
                    if line.startswith('def test_'):
                        test_names[task_id][method['method_name']].append(line[4:].split('(')[0])
        return test_names


class PathUtil:
    @staticmethod
    def get_name_string(model, task, pattern, task_level, context_level, cot_level, source, temperature):
        model_name = ModelEnum(model).name
        task_name = TaskEnum(task).name
        with_cot = "woCoT" if cot_level == 0 else f"wCoT{cot_level}"
        temp_str = str(int(temperature * 10))
        return f"{model_name}_{task_name}_{pattern}_task{task_level}_ctx{context_level}_{with_cot}_{source}_temp{temp_str}"

    @staticmethod
    def get_log_output_path(name_string):
        # make directory if it doesn't exist and avoid repeatedly creating
        log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'log'))
        os.makedirs(log_dir, exist_ok=True)
        return os.path.join(log_dir, f"{name_string}_log_output.log")

    @staticmethod
    def get_output_path(name_string):
        output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output'))
        os.makedirs(output_dir, exist_ok=True)
        return os.path.join(output_dir, f"{name_string}_output.json")

    @staticmethod
    def get_tmp_output_path(name_string, tmp_idx, method_name):
        tmp_output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tmp_output'))
        os.makedirs(tmp_output_dir, exist_ok=True)
        return os.path.join(tmp_output_dir, f"{name_string}_tmp_{tmp_idx}_{method_name}_output.json")

    @staticmethod
    def get_test_output_path(name_string):
        test_output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test'))
        os.makedirs(test_output_dir, exist_ok=True)
        return os.path.join(test_output_dir, f"{name_string}_test_output.json")

    @staticmethod
    def get_tmp_test_file_output_path():
        tmp_test_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tmp_test'))
        os.makedirs(tmp_test_dir, exist_ok=True)
        return tmp_test_dir

    @staticmethod
    def get_data_path():
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/ClassEval_data.json'))

class ModelEnum(Enum):
    GPT_3_5 = 0
    GPT_4 = 1
    ChatGLM = 2
    CodeGeex = 3
    WizardCoder = 4
    InCoder_1B = 5
    InCoder_6B = 6
    CodeBERT = 7
    CodeLlama = 8
    DeepSeekCoder = 9
    Llama3 = 10


class TaskEnum(Enum):
    Method_Generation = 0
    Adaptation = 1
