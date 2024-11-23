class DiscountStrategy:
    def due(self):
        """
        Calculate the final amount to be paid after applying the discount.
        :return: float, final amount to be paid
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> ds.due()
        312.55
    
        """
        amount = self.total()
        discount = 0
        if self.promotion:
            discount = self.promotion(amount)
        final_amount = amount - (amount * discount)
        return final_amount