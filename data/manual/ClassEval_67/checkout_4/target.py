class Order:
    def checkout(self):
        """
        Check out the dished ordered. If self.selected_dishes is not empty, invoke the calculate_total
        method to check out.
        :return False if the self.selected_dishes is empty, or total (return value of calculate_total) otherwise.
        """
        if not self.selected_dishes:
            return False
        else:
            return self.calculate_total()