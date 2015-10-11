__author__ = 'Dassa'

    # Attributes: responsible for knowing. Instance Variables
    # Methods: responsible for doing.


class Error(Exception):
    # Use this class to raise exceptions when code generates a runtime error
    def __init__(self, value):
        super().__init__(value)

class Country:
    # Use this class to represent the details about a single country
    def __init__(self, country_name, currency_code, currency_symbol):
        # defining attributes of the class
        self.country_name = country_name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol

    def format_currency(self, amount):
        return self.currency_symbol + str(format(float(amount), '.2f'))

    def __str__(self):
        return "Country Details: " + "{} {} {}".format(str(self.country_name) + str(self.currency_code) + str(self.currency_symbol))


class Details:
    def __init__(self):
        self.locations = []

    def add(self, country_name, start_date, end_date):
        details = (country_name, start_date, end_date)
        if details in self.locations:
            raise Error("Duplicate Trip")
        if start_date > end_date:
            raise Error("Date Error")
        self.locations.append(details)

    def current_country(self, date_string): #YYYY/MM/DD
        current_country = None
        for item in self.locations:
            # if date the date lies between two given dates, then your location is that corresponding location
            if item[1] < date_string < item[2]:
                current_country = item[0]
        if current_country is None:
            raise Error("Unrecorded Travel Date")
        else:
            return current_country






    # method is_empty() determines whether locations is empty or not
    def is_empty(self, locations):
        if locations == []:
            return True
        else:
            return False

details = Details()

aus_trip = ("Australia", "1997/11/08", "2015/10/11")
details.add("Australia", "1997/11/08", "2015/10/11")
print(details)














