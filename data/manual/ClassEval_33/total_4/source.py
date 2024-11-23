class DiscountStrategy:
    def total(cart):
        total_cost = 0
        for item in cart:
            total_cost += item['price']
        return total_cost