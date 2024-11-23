# ClassEval Benchmark

Thanks for FudanSELab for their crafted dataset. The original repository is [here](https://github.com/FudanSELab/ClassEval).

# Directory

- `ClassEval_data.json`

  The updated *ClassEval* dataset with several small issues fixed.

- `query.json`

  The method names and function descriptions of all the methods in the *ClassEval* dataset. We used them to create queries to retrieve code snippets.

- `retrieved.json`

  The generated code by GPT-3.5 with only the method name and its function description. We simulated the code retrieval from the online programming community by these snippets. For the subsequent adaptations, we picked the fourth (index 3) generated output as the method to be adapted.

- `random_list_200.json`

  We randomly picked 200 methods for test analysis and manual annotation.

- `benchmark/` DIR

  The folder for the original *ClassEval* benchmark solution and test code.

  - `benchmark_solution_code/` DIR
  - `benchmark_test_code/` DIR

- `manual/` DIR

  Automated labeled adaptation category and generated annotation files for each method.