class Order:
    def checkout(self):
        # Check if self.selected_dishes is not empty
        if self.selected_dishes:
            # Invoke the calculate_total method
            self.calculate_total()