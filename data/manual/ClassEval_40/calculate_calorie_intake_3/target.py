class FitnessTracker:
    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate),
        BMR is calculated based on the user's height, weight, age, and sex,
        male is 10 * self.weight + 6.25 * self.height - 5 * self.age + 5,
        female is 10 * self.weight + 6.25 * self.height - 5 * self.age - 161,
        and the calorie intake is calculated based on the BMR and the user's condition,
        if the user is too fat, the calorie intake is BMR * 1.2,
        if the user is too thin, the calorie intake is BMR * 1.6,
        if the user is normal, the calorie intake is BMR * 1.4.
        
        :return: calorie intake, float.
        """
        if self.sex == "male":
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        elif self.sex == "female":
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        
        if self.condition_judge() == "too fat":
            calorie_intake = bmr * 1.2
        elif self.condition_judge() == "too thin":
            calorie_intake = bmr * 1.6
        elif self.condition_judge() == "normal":
            calorie_intake = bmr * 1.4
        
        return calorie_intake