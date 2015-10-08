__author__ = 'Dassa'


import web_utility
import urllib
from urllib.request import urlopen
from urllib.error import URLError

# Convert function
def convert(amount, home_currency_code, location_currency_code):
    # url specific for any provided amount, home and location currency codes.
    url = "https://www.google.com/finance/converter?a=" + str(amount) + "&from=" + str(home_currency_code) + "&to=" + str(location_currency_code) + "&meta=ei%3Db-INVuGzDsy60gSThqFg"
    # returns the information provided by the given url
    result = web_utility.load_page(url)
    # initial shortening of result
    strip_result = (result[result.index('result'):])
    parts = strip_result.split(">")
    split_parts = parts[2].split(" ")
    return_amount = split_parts[0]
    return return_amount

    # TODO if function is used incorrectly, return the value '-1'

# Convert function Trial
# set parameters
amount = ""      # returns as if = 1 when a string of letters is inserted
home_currency_code = "USD"
location_currency_code = "SCR"
# call function
print(convert(amount, home_currency_code, location_currency_code))
# print function

# # input parameters
# return_amount = convert(input("amount: "), input("home_currency_code: "), input("location_currency_code: "))
# # print function
# print(return_amount)

# Get Details function
def get_details(country_name):
    # set empty variables
    finish = False      # consider: running / looking = True (affirmative boolean)
    i = 0       # position variable
    country_details_list = None
    # open currency_details.txt file in read only mode
    currency_details = open("currency_details.txt", mode="r", encoding="utf-8")

    for line in currency_details.readlines():
            parts = line.strip().split(",")
            if parts[0] == country_name:
                country_details_ea = tuple(parts)
                return country_details_ea

# # Get Details function trial
# # Set parameters
# country_name = "United States"      # use title() method
# # Call function
# country_details_ea = get_details(country_name)
# # Print function
# print(country_details_ea)
#
# # input parameters
# country_details_ea = get_details(input("country_name: "))
# # Print function
# print(country_details)