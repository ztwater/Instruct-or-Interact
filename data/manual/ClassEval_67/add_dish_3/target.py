class Order:
    def add_dish(self, dish):
        for item in self.menu:
            if item['dish'] == dish['dish']:
                count = item['count']
                if count >= dish['count']:
                    self.selected_dishes.append(dish)
                    item['count'] -= dish['count']
                    return True
        return False