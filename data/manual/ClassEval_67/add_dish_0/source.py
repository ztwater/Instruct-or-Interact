class Order:
    def add_dish(self, dish):
        if dish in self.menu:
            count = self.menu[dish]
            if count > 0:
                self.selected_dish.append(dish)
                self.menu[dish] -= 1
                return True
        return False