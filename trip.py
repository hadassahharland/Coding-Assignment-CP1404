import currency
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

    def __str__(self):
        return "{} {} {}".format(str(self.country_name), str(self.currency_code), str(self.currency_symbol))

    def format_currency(self, amount):
        # Format amount to be presented as %X.XX where % is the
        return self.currency_symbol + str(format(float(amount), '.2f'))


class Details:
    # Use this class to determine dates and locations relevant to the trip
    def __init__(self):
        self.locations = []

    def add(self, country_name, start_date, end_date):
        trip_details = (country_name, start_date, end_date)
        # check for invalid dates
        dates = [start_date.split("/"), end_date.split("/")]
        for item in dates:
            # check every character in the date, without the separators, is a digit
            for part in item:
                for char in part:
                    if not char.isdigit():
                        raise Error("Invalid date")
            # check the length of the year is 4 digits, and the date and months are 2 digits
            if len(item[0]) != 4 or len(item[1]) != 2 or len(item[2]) != 2:
                raise Error("Invalid date")
        if trip_details in self.locations:
            raise Error("Duplicate Trip")
        if start_date > end_date:
            raise Error("Invalid date")
        self.locations.append(trip_details)

    def current_country(self, date_string):
        # Date format YYYY/MM/DD
        current_country = None
        for item in self.locations:
            # if date the date lies between two given dates, then your location is that corresponding location
            if item[1] < date_string < item[2]:
                current_country = item[0]
        if current_country is None:
            raise Error("Unrecorded Travel Date")
        else:
            return current_country

    # method is_empty() determines whether locations is empty or not, and returns true if empty
    def is_empty(self):
        return self.locations == []

# Testing
def main():
    print("Check Country Class")
    print("Format: Australia, AUD, $, amount = 100  " + Country("Australia", "AUD", "$").format_currency(100))
    print("\nCheck Details Class")
    details = Details()
    details.add("Australia", "2000/01/01", "2015/01/01")
    print(details.locations)
# TODO further error checking
# use a try/except for the invalid things that raise errors...
if __name__ == "__main__":
    main()