class DiscountStrategy:
    def BulkItemPromo(order):
        if order.cart[0]['quantity'] >= 20:
            discount = 0.1
        else:
            discount = 0
        return discount