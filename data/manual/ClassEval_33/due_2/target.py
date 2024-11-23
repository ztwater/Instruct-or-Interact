class DiscountStrategy:
    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        """
        amount = self.total()  # Calculate the total amount of the order
        discount = 0
        
        if self.promotion is not None:  # Check if a promotion function is provided
            discount = self.promotion(self.cart)  # Apply the promotion function to calculate the discount
        
        final_amount = amount - (amount * discount)  # Calculate the final amount to be paid
        
        return final_amount