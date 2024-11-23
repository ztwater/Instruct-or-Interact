class DiscountStrategy:
    def FidelityPromo(fidelity_points, order_total):
        if fidelity_points > 1000:
            discount = order_total * 0.05
            return discount
        else:
            return 0