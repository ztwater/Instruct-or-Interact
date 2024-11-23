class DiscountStrategy:
    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        
        """
        amount = sum(item['quantity'] * item['price'] for item in self.cart)
        discount = self.promotion(self.cart)
        final_amount = amount - (amount * discount)
        return final_amount