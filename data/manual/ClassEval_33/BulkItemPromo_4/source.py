class DiscountStrategy:
    def BulkItemPromo(quantity):
        if quantity >= 20:
            discount = 0.1
        else:
            discount = 0
        return discount