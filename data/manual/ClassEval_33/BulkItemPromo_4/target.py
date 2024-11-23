class DiscountStrategy:
    def BulkItemPromo(order):
        """
        Calculate the discount based on bulk item quantity in the order.In the same order, if the quantity of a single item reaches 20 or more, each item will enjoy a 10% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        """
        quantity = sum(item['quantity'] for item in order.cart)
        if quantity >= 20:
            discount = 0.1
        else:
            discount = 0
        return discount