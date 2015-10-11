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
        # Format amount to be presented as %X.XX where % is the amount
        try:
            return self.currency_symbol + str(format(float(amount), '.2f'))
        except ValueError:
            raise Error("Invalid amount")


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
        # raise error if dates overlap
        for trip in self.locations:
            for thing in trip:
                if start_date <= thing <= end_date:
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
    print("Valid format     Format: Australia,      AUD, $, amount = 100      " + Country("Australia", "AUD", "$").format_currency(100))
    print("Valid format     Format: United States,  USD, $, amount = 42.43    " + Country("United States", "USD", "$").format_currency(42.43))
    print("Valid format     Format: Slovenia,       EUR, €, amount = 199.9    " + Country("Slovenia", "USD", "€").format_currency(199.9))
    try:
        print("Valid format   Format: Australia,      AUD, $, amount = abc       " + Country("Australia", "AUD", "abc").format_currency(abc))
    except:
        print("Invalid format   Format: Australia,      AUD, $, amount = abc      Error: Invalid Amount")

    print("\nCheck Details Class")
    details = Details()
    print("Empty locations                                          ", details.locations)
    details.add("Australia", "2002/01/01", "2003/01/01")
    print("Valid addition       Australia, 2002/01/01, 2003/01/01   ", details.locations)
    details.add("Japan", "2004/02/23", "2004/02/24")
    print("Valid addition       Japan, 2004/02/23, 2004/02/24       ", details.locations)
    try:
        details.add("Japan", "2004/02/23", "2004/02/24")
        print("Valid addition       ", details.locations)
    except:
        print("Invalid addition     Japan, 2004/02/23, 2004/02/24        Duplicate trip")

    details.add("Japan", "2005/02/23", "2005/02/24")
    print("Valid addition       Japan, 2005/02/23, 2005/02/24       ", details.locations)
    try:
        details.add("France", "2004/02/23", "2004/02/24")
        print("Valid addition       ", details.locations)
    except:
        print("Invalid addition     France, 2004/02/23, 2004/02/24       Invalid Dates")
    try:
        details.add("France", "06/12/07", "2006/12/13")
        print("Valid addition       ", details.locations)
    except:
        print("Invalid addition     France, 06/12/07, 2006/12/13         Invalid Dates")
    try:
        details.add("Australia", "2006/01/02", "2006/Ja/04")
        print("Valid addition       ", details.locations)
    except:
        print("Invalid addition     Australia, 2006/01/02, 2006/Ja/04    Invalid Dates")
    try:
        details.add("Germany", "2006/12/02", "2006/01/04")
        print("Valid addition       ", details.locations)
    except:
        print("Invalid addition     Germany, 2006/12/02, 2006/01/04      Invalid Dates")
    details.add("Germany", "2005/12/02", "2006/01/04")
    print("Valid addition       Germany, 2005/12/02, 2006/01/04     ", details.locations)

if __name__ == "__main__":
    main()
