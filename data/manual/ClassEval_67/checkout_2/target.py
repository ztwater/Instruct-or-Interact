class Order:
    def checkout(self):
        if self.selected_dishes:
            total = self.calculate_total()
            return total
        else:
            return False