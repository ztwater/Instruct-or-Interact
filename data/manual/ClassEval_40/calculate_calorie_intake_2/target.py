class FitnessTracker:
    def calculate_calorie_intake(self):
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