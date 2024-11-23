class FitnessTracker:
    def calculate_calorie_intake(height, weight, age, sex, condition):
        if sex == "male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        elif sex == "female":
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        
        if condition == "too fat":
            calorie_intake = bmr * 1.2
        elif condition == "too thin":
            calorie_intake = bmr * 1.6
        elif condition == "normal":
            calorie_intake = bmr * 1.4
        
        return calorie_intake