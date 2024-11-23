### Method Description:
    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.condition_judge()
        -1

        """

### Solution Code:
    def condition_judge(self):
        BMI = self.get_BMI()
        if self.sex == "male":
            BMI_range = self.BMI_std[0]["male"]
        else:
            BMI_range = self.BMI_std[1]["female"]
        if BMI > BMI_range[1]:
            # too fat
            return 1
        elif BMI < BMI_range[0]:
            # too thin
            return -1
        else:
            # normal
            return 0

### Source Code:
    def condition_judge(weight, height):
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            return "Underweight"
        elif bmi >= 18.5 and bmi < 24.9:
            return "Normal weight"
        elif bmi >= 24.9 and bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

### Predicted Code:
    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        """
        bmi = self.weight / (self.height ** 2)
        
        if self.sex == "male":
            bmi_range = self.BMI_std[0]["male"]
        else:
            bmi_range = self.BMI_std[1]["female"]

        if bmi < bmi_range[0]:
            return -1
        elif bmi >= bmi_range[0] and bmi < bmi_range[1]:
            return 0
        else:
            return 1

### Adaptation:
Total number: 54
### Raw Output:
```
    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        """
        bmi = self.weight / (self.height ** 2)
        
        if self.sex == "male":
            bmi_range = self.BMI_std[0]["male"]
        else:
            bmi_range = self.BMI_std[1]["female"]

        if bmi < bmi_range[0]:
            return -1
        elif bmi >= bmi_range[0] and bmi < bmi_range[1]:
            return 0
        else:
            return 1
```

### Test Code:
class FitnessTrackerTestConditionJudge(unittest.TestCase):
    def test_condition_judge(self):
        fitnessTracker = FitnessTracker(1.8, 45, 20, "female")
        self.assertEqual(fitnessTracker.condition_judge(), -1)

    def test_condition_judge_2(self):
        fitnessTracker = FitnessTracker(1.72, 80, 22, "female")
        self.assertEqual(fitnessTracker.condition_judge(), 1)

    def test_condition_judge_3(self):
        fitnessTracker = FitnessTracker(1.72, 53, 22, "male")
        self.assertEqual(fitnessTracker.condition_judge(), -1)

    def test_condition_judge_4(self):
        fitnessTracker = FitnessTracker(1.72, 60, 22, "male")
        self.assertEqual(fitnessTracker.condition_judge(), 0)

    def test_condition_judge_5(self):
        fitnessTracker = FitnessTracker(1.72, 75, 22, "male")
        self.assertEqual(fitnessTracker.condition_judge(), 1)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.BMI_std, self.sex
# method_dependencies: get_BMI


