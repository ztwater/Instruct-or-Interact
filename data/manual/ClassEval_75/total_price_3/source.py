class ShoppingCart:
    def total_price(shopping_list):
        total = 0
        for item in shopping_list:
            quantity = item['quantity']
            price = item['price']
            total += quantity * price
        return total