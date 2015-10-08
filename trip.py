__author__ = 'Dassa'

    # Attributes: responsible for knowing. Instance Variables
    # Methods: responsible for doing.


class Error(Exception):
    # Use this class to raise exceptions when code generates a runtime error
    def __init__(self, value):
        super().__init__(value)
    # Exceptions must have appropriate descriptions for the Exception.value field
    pass

class Country:
    # Use this class to represent the details about a single country
    def __str__(self):
        # returns a string containing the country details; object Country("name","EUR","€") generates the string "Germany EUR €"
        pass
    def name(self):
        self.name = name       # (0) in the tuple given by get_details
        # name needs to be a string using .title()
        pass
    def currency_code(self):
        self.currency_code = currency_code      # (1) in the tuple given by get_details
        # currency_code needs to be a string of length 3.
        pass
    def currency_symbol(self):
        self.currency_symbol = currency_symbol      # (2) in the tuple given by get_details
        # currency_symbol needs to be unformatted
        pass

class details:
    def __init__(self):
        self.locations = locations      # list or dictionary used to store the trip details

    self.current_country(date_string)
    pass






















