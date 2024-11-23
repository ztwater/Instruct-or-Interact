# Instruct-or-Interact
Replication package of ICSE 2025 paper "Instruct or Interact? Exploring and Eliciting LLMs’ Capability in Code Snippet Adaptation Through Prompt Engineering".

---

## Installation

Run the following command to install required dependencies

```bash
pip install -r requirements.txt
```

---

## Run the inference

```bash
cd src

# adaptation (GPT-3.5 in instruction prompt)
python run.py --data_path ../data/retrieved.json --pattern instruction --task 1 --task_level 0 --context_level 1 --cot_level 0 --repeat 5 --model 0 --source api --temperature 0.8
```

The `pattern` parameter describes the prompt style, including `direct` (the text same as the input text), `instruction` (the instruction prompt used in our empirical study), `enhanced` (enhanced prompt with task decomposition),`human` for Human-LLM interaction, `mac` and `mae` for multi-agent prompt with counselor or evaluator.

The `task` parameter describe the task is generation (0) or adaptation (1).

The `task_level`, `context_level` and `cot_level` describe the information provided in the prompt. The detail settings are in the `prompt_loader.py` and `utils.py`.

The `model` parameter describes which LLM is used.

The `source` parameter serves as a label in the name string of the output file.

---

## Run the test

```bash
cd src

# adaptation (GPT-3.5 in instruction prompt)
python test.py  --pattern instruction --task 1 --task_level 0 --context_level 1 --cot_level 0 --repeat 5 --model 0 --source api --temperature 0.8
```

The test script share almost the same parameters with the inference script, which could be used to obtain the evaluation results directly from the inference output (without re-running the inference script).

---

## To reproduce our results

### 1. RQ1: Re-run from inference phase

For each model with different parameter and temperature settings, run the inference script  with the following command:

```shell
cd src

# LLM adaptations
# --model: 0(GPT-3.5) 8(CodeLlama) 10(Llama-3)
# --source: 7b, 8b, 13b, 34b, api, ... It is a field for label.
# --temperature: 0, 0.2, 0.4, 0.6, 0.8, 1.0
python run.py --data_path ../data/retrieved.json --pattern instruction --task 1 --context_level 1 --repeat 5 --model MOD --source Xb --temperature TEMP


# GPT-3.5 generation (baseline)
# --temperature: 0, 0.2, 0.4, 0.6, 0.8, 1.0
python run.py --pattern instruction --context_level 1  --repeat 5 --model 0 --source api --temperature TEMP
```

Outputs can be found in `./src/output`, test results are can be found in `./src/test`.

### 2. RQ1: Re-run our results (test only)

```shell
# copy results to output dir
cp ./result/RQ1/MODEL/PARAM/XXX.json ./src/output/

cd src

# LLM adaptations
# --model: 0(GPT-3.5) 8(CodeLlama) 10(Llama-3)
# --source: 7b, 8b, 13b, 34b, api, ... It is a field for label.
# --temperature: 0, 0.2, 0.4, 0.6, 0.8, 1.0
python test.py --pattern instruction --task 1 --context_level 1 --repeat 5 --model MOD --source SRC --temperature TEMP

# GPT-3.5 generation (baseline)
# --temperature: 0, 0.2, 0.4, 0.6, 0.8, 1.0
python test.py --pattern instruction --context_level 1  --repeat 5 --model 0 --source api --temperature TEMP
```

Test results are can be found in `./src/test`.

### 3. RQ2+RQ3: Manual Annotation

See `./results/RQ2+3/manual_annotation.xlsx`.

### 4. Evaluation Results For Interactive Prompting

#### 4.1 Ablation Study

```shell
cd src

# Enhanced
python run.py --data_path ../data/retrieved.json --pattern enhanced --task 1 --context_level 3 --cot_level 1 --repeat 5 --source api --temperature 0.8

# Ablation
--context_level 1: without docstring & code
--cot_level 0: without dependency
--pattern instruction: without task decomposition
```

#### 4.2 Mitigation of Bugs

See `./results/Evaluation/mitigation_of_bugs/manual_annotation.xlsx`.

#### 4.3 Multi-Agent Interactions

```shell
cd src

# Human-LLM
# --model: 0 for GPT-3.5 (default)
# --source: manual, ... It is a field for label.
# --temperature: 0.8 for GPT-3.5
python run.py --data_path ../data/retrieved.json --pattern human --task 2 --context_level 3 --cot_level 2 --repeat 5 --source manual --temperature 0.8

# MAE
# --model: 0 for GPT-3.5 (default)
# --source: manual, ... It is a field for label.
# --temperature: 0.8 for GPT-3.5
python run.py --data_path ../data/retrieved.json --pattern mae --task 0 --context_level 3 --cot_level 1 --repeat 5 --source manual --temperature 0.8

# MAC
# --model: 0(GPT-3.5) 8(CodeLlama) 10(Llama-3)
# --source: 8b, 34b, api, manual, ... It is a field for label.
# --temperature: 0.8 for GPT-3.5, 0.6 for CodeLlama-34B, Llama-3-8B
python run.py --data_path ../data/retrieved.json --pattern mac --task 2 --context_level 3 --cot_level 1 --repeat 5 --model MOD --source SRC --temperature TEMP
```
