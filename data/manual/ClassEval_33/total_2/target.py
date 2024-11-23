class DiscountStrategy:
    def total(self):
        total_cost = 0
        for item in self.cart:
            total_cost += item['price']
        return total_cost