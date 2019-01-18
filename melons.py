"""Classes for melon orders."""

class AbstractMelonOrder():
    """ An abstract base class that other Melon Orders inherit from """

    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.flat_fee = 0
        if country_code:
            self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas":
            base_price = 1.5*base_price

        total = (1 + self.tax) * self.qty * base_price + self.flat_fee

        return total
    

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.tax = 0.17
        if self.qty < 10:
            self.flat_fee = 3

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """ """

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False
        self.tax = 0.00

    def mark_inspection(self, status=False):
        self.passed_inspection = status
