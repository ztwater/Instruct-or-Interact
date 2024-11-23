class DiscountStrategy:
    def LargeOrderPromo(order):
        num_products = len(order.cart)
        if num_products >= 10:
            discount = 0.07
        else:
            discount = 0.00
        return discount