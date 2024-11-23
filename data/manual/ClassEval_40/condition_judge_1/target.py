class FitnessTracker:
    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.condition_judge()
        -1
    
        """
        bmi = self.get_BMI()
    
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