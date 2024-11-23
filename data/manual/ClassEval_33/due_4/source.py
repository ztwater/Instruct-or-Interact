class DiscountStrategy:
    def due(amount, discount):
        final_amount = amount - (amount * discount)
        return final_amount