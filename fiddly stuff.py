__author__ = 'Dassa'


import web_utility
import urllib
from urllib.request import urlopen
from urllib.error import URLError


def convert(amount, home_currency_code, location_currency_code):
    url = "https://www.google.com/finance/converter?a=" + str(amount) + "&from=" + str(home_currency_code) + "&to=" + str(location_currency_code) + "&meta=ei%3Db-INVuGzDsy60gSThqFg"
    result = web_utility.load_page(url)
    strip_result = (result[result.index('result'):])
    print(strip_result)
    return result


convert(1, "AUD", "USD")


# tutorname = "trevor andersen"




        ## get a string input from the user for the value of the money they wish to convert
        ## Convert string input to float value
        ## Store input under the variable name currency_amount_input
# currency_amount_input = float(input("Currency Amount Input: "))
#         ## For testing: Bypasses user input
# currency_amount_input = float(1)
# #     ValueError
#
#         ## get a string input from the user for the name of the country
# # inputcountrycode = input("Country Code From: ")
# # outputcountrycode = input("Country Code To: ")
#
#
# inputcountrycode = "AUD"
# outputcountrycode = "USD"
#
# url = "https://www.google.com/finance/converter?a=" + str(currency_amount_input) + "&from=" + inputcountrycode + "&to=" + outputcountrycode + "&meta=ei%3Db-INVuGzDsy60gSThqFg"
# print (url)
#
# # f = urllib.urlopen(link)
# # myfile = f.read()
# # print (myfile)
# # print(link)
#

#
#
# def get_details(country_name):
#     country_name = ""
#     currency_details = open("currency_details.txt", mode="r", encoding="utf-8")
#     file_contents = currency_details.read()
#
#
#
# currency_details = open("currency_details.txt", mode="r", encoding="utf-8")
# country_name = input("Country name: ")
#
# finish = ""
# country_details = ""
# i = 0
# while finish == "":
#     line = currency_details.readline()
#     if country_name in line:
#         finish = "True"
#             # refresh currency_details file
#         currency_details.close()
#         currency_details = open("currency_details.txt", mode="r", encoding="utf-8")
#         currency_details = currency_details.readlines()
#     else:
#         i += 1

#
# details_tuple = tuple(currency_details)
# print (details_tuple)



# if country_details == ""
#     print("Country does not exist")
# else:
#     print(country_details[i])
#
#
#
#
#
# for line in currency_details:
#     If country_name in currency_details.readline():
#         finish = "True"
#     else
#         i += 1
# trial from internets
# with open("currency_details.txt") as f:
#     data = [tuple(line) for line in txt.reader(f)]
#
# print(data)














