class FitnessTracker:
    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        """
        bmi = self.weight / (self.height ** 2)

        if self.sex == "male":
            male_std = self.BMI_std[0]["male"]
            if bmi < male_std[0]:
                return -1
            elif bmi >= male_std[0] and bmi < male_std[1]:
                return 0
            else:
                return 1
        elif self.sex == "female":
            female_std = self.BMI_std[1]["female"]
            if bmi < female_std[0]:
                return -1
            elif bmi >= female_std[0] and bmi < female_std[1]:
                return 0
            else:
                return 1
        else:
            return None