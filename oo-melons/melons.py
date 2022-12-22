"""Classes for melon orders."""
# create super class AbstractMelonOrder 
# add shared methods

class AbstractMelonOrder():
    
    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty) # had to have these two arguments still to match parent class 
         

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        # self.species = species
        # self.qty = qty
        # self.shipped = False
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
