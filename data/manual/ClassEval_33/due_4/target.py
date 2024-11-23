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

        # Calculate the total amount of the items in the cart
        total_amount = self.total()

        # Apply the promotion function if provided
        if self.promotion:
            total_amount = self.promotion(total_amount)

        return total_amount

