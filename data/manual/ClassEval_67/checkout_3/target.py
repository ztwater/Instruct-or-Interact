class Order:
    def checkout(self):
        """
        Check out the dishes ordered. If self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return False if self.selected_dishes is empty, or total (return value of calculate_total) otherwise.
        """
        if not self.selected_dishes:
            return False
        return self.calculate_total()