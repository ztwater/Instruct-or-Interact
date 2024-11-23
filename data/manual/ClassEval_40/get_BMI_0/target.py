class FitnessTracker:
    def get_BMI(self):
        """
        Calculate the BMI based on the height and weight.
        :return: BMI,which is the weight divide by the square of height, float.
        """
        bmi = self.weight / (self.height ** 2)
        return bmi