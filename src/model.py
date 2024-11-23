import time
import openai
from openai.error import RateLimitError
from random import choice
import re
# from tenacity import retry, stop_after_attempt, wait_random_exponential, RetryError
from utils import ModelEnum
import tiktoken
from utils import DataUtil

class GPT:
    def __init__(self, model, temperature, max_length):
        self.keys = ["sk-123456"]
        # self.keys = self.get_api_keys()
        self.model = model
        self.temperature = temperature
        self.max_length = max_length

    # @retry(wait=wait_random_exponential(multiplier=10, max=60), stop=stop_after_attempt(5), reraise=True)
    # def completion_with_backoff(self, **kwargs):
    #     return openai.ChatCompletion.create(**kwargs)

    @staticmethod
    def get_api_keys():
        with open("api_key.txt", encoding='utf-8') as file:
            api_keys = file.readlines()
            api_keys = [key.strip() for key in api_keys]  # remove the '\n' at the end of each line
        return api_keys

    def send_request(self, message_history):
        tmp_key = choice(self.keys)
        # openai.api_base = "https://api.openai.com/v1"
        openai.api_base = "https://localhost:1234/v1"
        openai.api_key = tmp_key
        prompt_string = ''.join([m['content'] for m in message_history if m['role'] != 'system'])
        # handle the length limit
        if self.model == ModelEnum.GPT_3_5.value:
            encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
            num_tokens = len(encoding.encode(prompt_string))
            print(f"Prompt token count: {num_tokens}")
            if num_tokens > 2000:
                print("Prompt length exceeds the limit of 4k model, using 16k model instead.")
                model_str = "gpt-3.5-turbo-16k-0613"
            else:
                model_str = "gpt-3.5-turbo-0613"
        elif self.model == ModelEnum.GPT_4.value:
            model_str = "gpt-4"
        else:
            raise ValueError("Model not supported")
        max_retries = len(self.keys)
        retry_count = 0
        while retry_count < max_retries:
            try:
                response = openai.ChatCompletion.create(
                    model=model_str,
                    messages=message_history,
                    temperature=self.temperature,
                    max_tokens=self.max_length,
                    # request_timeout=60
                )
                break
            except RateLimitError as e:
                if 'requests per day' in str(e):
                    self.keys.remove(tmp_key)
                    tmp_key = choice(self.keys)
                    print(f"Daily rate limit error with {openai.api_key}. Change to {tmp_key}.")
                    openai.api_key = tmp_key
                elif 'requests per min' in str(e) or 'tokens per min' in str(e):
                    print(f"Minute rate limit error with {openai.api_key}, wait 60s.")
                    time.sleep(60)
                elif 'exceeded your current quota' in str(e):
                    self.keys.remove(tmp_key)
                    tmp_key = choice(self.keys)
                    print(f"Quota exceeded with {openai.api_key}. Change to {tmp_key}.")
                    openai.api_key = tmp_key
                else:
                    print("Unknown rate limit error.")
                    raise e
                retry_count += 1
            except Exception as e:
                print(e)
                retry_count += 1
            print(f"Retry count: {retry_count}")
        else:
            raise Exception("All keys are used up or an unknown exception exists, please check the output.")
        return response["choices"][0]["message"]["content"]

    def run_prompts(self, prompts):
        message_history = [{"role": "system", "content": "You are a helpful assistant."}]
        for prompt in prompts:
            message_history.append({"role": "user", "content": prompt})
            output = self.send_request(message_history)
            message_history.append({"role": "assistant", "content": output})
        return message_history

    def run_prompts_human(self, prompts):
        message_history = [{"role": "system", "content": "You are a professional developer in Python programming. Your task is to understand the code context, raise questions if needed and generate the adapted code based on the provided answers to the questions."}]
        turn = 0
        while True:
            print(f"Turn {turn}:")
            if len(prompts) > turn:
                prompt = prompts[turn]
            else:
                last_output = message_history[-1]['content']
                try:
                    print("assistant:\n" + last_output + "\n")
                except Exception as e:
                    print(e)
                # break if LLM provide the code
                if re.search(r"```", last_output) and re.search(r"def\s\w+\(", last_output):
                    break
                prompt = input("User: ")
            message_history.append({"role": "user", "content": prompt})
            output = self.send_request(message_history)
            message_history.append({"role": "assistant", "content": output})
            turn += 1
        return message_history

    def run_prompts_mac(self, prompts):
        message_history_0 = [{"role": "system", "content": "You are a professional developer in Python programming. Your task is to understand the code context, raise questions if needed and generate the adapted code based on the provided answers to the questions."}]
        message_history_1 = [{"role": "system", "content": "You are a helpful counselor with professional experience in Python programming. Your primary task is to understand the code context, review the retrieved snippets, and generate helpful answers to the provided questions."}]
        print("Turn 0:")
        # context comprehension for both LLMs
        message_history_0.append({"role": "user", "content": prompts[0]})
        message_history_1.append({"role": "user", "content": prompts[0]})
        output = self.send_request(message_history_0)
        message_history_0.append({"role": "assistant", "content": output})
        message_history_1.append({"role": "assistant", "content": output})
        print("Turn 1:")
        # LLM1 asks the questions and LLM2 answers
        message_history_0.append({"role": "user", "content": prompts[1]})
        output = self.send_request(message_history_0)
        message_history_0.append({"role": "assistant", "content": output})
        if re.search(r"```", output) and re.search(r"def\s\w+\(", output):
            return message_history_0
        message_history_1.append({"role": "user", "content": re.sub(r'QUESTION_PLACEHOLDER', lambda m: output, prompts[2])})
        output = self.send_request(message_history_1)
        message_history_1.append({"role": "assistant", "content": output})
        print("Turn 2:")
        # LLM1 generates the code based on LLM2's answer
        message_history_0.append({"role": "user", "content": re.sub(r'ANSWER_PLACEHOLDER', lambda m: output, prompts[3])})
        output = self.send_request(message_history_0)
        message_history_0.append({"role": "assistant", "content": output})
        return message_history_0

    def run_prompts_mae(self, method_name, prompts):
        message_history_0 = [{"role": "system", "content": "You are a professional developer in Python programming. Your task is to understand the code context, raise questions if needed and generate the adapted code based on the provided answers to the questions."}]
        message_history_1 = [{"role": "system", "content": "You are a helpful evaluator with professional experience in Python programming. Your task is to review the adaptation, identify any issues, and provide feedback or instructions for further refinement."}]
        print("Turn 0:")
        # context comprehension for both LLMs
        message_history_0.append({"role": "user", "content": prompts[0]})
        message_history_1.append({"role": "user", "content": prompts[0]})
        output = self.send_request(message_history_0)
        message_history_0.append({"role": "assistant", "content": output})
        message_history_1.append({"role": "assistant", "content": output})
        print("Turn 1:")
        # LLM1 asks the questions and LLM2 answers
        message_history_0.append({"role": "user", "content": prompts[1]})
        output = self.send_request(message_history_0)
        message_history_0.append({"role": "assistant", "content": output})
        method_code = DataUtil.extract_method_from_output(output, method_name)
        if method_code == '':
            evaluation_prompt = f"Please generate the adapted method {method_name} with correct signature again."
        else:
            evaluation_prompt = re.sub(r'METHOD_PLACEHOLDER', lambda m: method_code, prompts[2])
        message_history_1.append({"role": "user", "content": evaluation_prompt})
        output = self.send_request(message_history_1)
        message_history_1.append({"role": "assistant", "content": output})
        message_history_0.append({"role": "user", "content": re.sub(r'ISSUE_PLACEHOLDER', lambda m: output, prompts[3])})
        output = self.send_request(message_history_0)
        message_history_0.append({"role": "assistant", "content": output})
        return message_history_0
