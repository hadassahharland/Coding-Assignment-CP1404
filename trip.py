__author__ = 'Dassa'

    # Attributes: responsible for knowing. Instance Variables
    # Methods: responsible for doing.


class Error(Exception):
    # Use this class to raise exceptions when code generates a runtime error
    def __init__(self, value):
        super().__init__(value)
    # Exceptions must have appropriate descriptions for the Exception.value field
    # If an error is called the raise statement creates an Error exception object

class Country:
    # Use this class to represent the details about a single country
    def __init__(self, name, currency_code, currency_symbol):
        # defining attributes of the class
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol

    def __str__(self):
        # returns a string containing the country details; object Country("name","EUR","€") generates the string "Germany EUR €"


class Details:
    def __init__(self):
        self.locations = []      # list or dictionary used to store the trip details

    def add(self, country_name, start_date, end_date):
        self.country_name = country_name
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):

    def current_country(self, date_string):
        #YYYY/MM/DD

        date_list = date_string.split("/")
        if

    # method is_empty() determines whether locations is empty or not
    def is_empty(self, locations):
        if locations == []:
            return True
        else:
            return False






















