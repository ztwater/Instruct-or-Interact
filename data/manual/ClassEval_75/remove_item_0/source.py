class ShoppingCart:
    def remove_item(shopping_list, item, quantity):
        if item in shopping_list:
            current_quantity = shopping_list[item]
            if current_quantity >= quantity:
                shopping_list[item] -= quantity
                print(f"Successfully removed {quantity} {item}(s) from the shopping list.")
            else:
                print(f"Error: There are only {current_quantity} {item}(s) in the shopping list.")
        else:
            print(f"Error: {item} is not in the shopping list.")
    