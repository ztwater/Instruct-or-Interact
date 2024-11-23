class FitnessTracker:
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