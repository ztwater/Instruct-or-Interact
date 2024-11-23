### Method Description:
    @staticmethod
    def FidelityPromo(order):
        """
        Calculate the discount based on the fidelity points of the customer.Customers with over 1000 points can enjoy a 5% discount on the entire order.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> DiscountStrategy.FidelityPromo(order)
        16.45

        """

### Solution Code:
    @staticmethod
    def FidelityPromo(order):
        return order.total() * 0.05 if order.customer['fidelity'] >= 1000 else 0

### Source Code:
    def FidelityPromo(fidelity_points, order_total):
        if fidelity_points > 1000:
            discount = order_total * 0.05
            return discount
        else:
            return 0

### Predicted Code:
    def FidelityPromo(order):
        """
        Calculate the discount based on the fidelity points of the customer.Customers with over 1000 points can enjoy a 5% discount on the entire order.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> DiscountStrategy.FidelityPromo(order)
        16.45
        """
        fidelity_points = order.customer.get('fidelity', 0)
        order_total = order.total()
        if fidelity_points > 1000:
            discount = order_total * 0.05
            return discount
        else:
            return 0

### Adaptation:
Total number: 15
### Raw Output:
```
class DiscountStrategy:  
    """
    This is a class that allows to use different discount strategy based on shopping credit or shopping cart in supermarket.
    """

    def __init__(self, customer, cart, promotion=None):
        """
        Initialize the DiscountStrategy with customer information, a cart of items, and an optional promotion.
        :param customer: dict, customer information
        :param cart: list of dicts, a cart of items with details
        :param promotion: function, optional promotion applied to the order
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        """
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self.total()

    def total(self):
        pass

    def due(self):
        pass

    def BulkItemPromo(order):
        pass

    def LargeOrderPromo(order):
        pass

    @staticmethod
    def FidelityPromo(order):
        """
        Calculate the discount based on the fidelity points of the customer.Customers with over 1000 points can enjoy a 5% discount on the entire order.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> DiscountStrategy.FidelityPromo(order)
        16.45
        """
        fidelity_points = order.customer.get('fidelity', 0)
        order_total = order.total()
        if fidelity_points > 1000:
            discount = order_total * 0.05
            return discount
        else:
            return 0
```

### Test Code:
class DiscountStrategyTestFidelityPromo(unittest.TestCase):
    def test_fidelity_promo_1(self):
        customer = {'name': 'John Doe', 'fidelity': 1000}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_discount = 12.5
        actual_discount = order.promotion(order)
        self.assertEqual(actual_discount, expected_discount)

    def test_fidelity_promo_2(self):
        customer = {'name': 'John Doe', 'fidelity': 800}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_discount = 0
        actual_discount = order.promotion(order)
        self.assertEqual(actual_discount, expected_discount)

    def test_fidelity_promo_3(self):
        customer = {'name': 'John Doe', 'fidelity': 0}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_discount = 0
        actual_discount = order.promotion(order)
        self.assertEqual(actual_discount, expected_discount)

    def test_fidelity_promo_4(self):
        customer = {'name': 'John Doe', 'fidelity': 10000}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_discount = 12.5
        actual_discount = order.promotion(order)
        self.assertEqual(actual_discount, expected_discount)

    def test_fidelity_promo_5(self):
        customer = {'name': 'John Doe', 'fidelity': 1800}
        cart = [{'product': 'product1', 'quantity': 10, 'price': 20.0},
                {'product': 'product2', 'quantity': 5, 'price': 10.0}]
        order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        expected_discount = 12.5
        actual_discount = order.promotion(order)
        self.assertEqual(actual_discount, expected_discount)

### Test Output:
# 0 errors, 1 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_fidelity_promo_1: 0 != 12.5


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: total


