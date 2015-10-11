import web_utility

__author__ = 'Dassa'
# manipulating program to run main() function
# __name__ = '__main__'


def convert(amount, home_currency_code, location_currency_code):
    # url specific for any provided amount, home and location currency codes.
    try:
        float(amount)
        url = "https://www.google.com/finance/converter?a=" + str(amount) + "&from=" + str(home_currency_code) + "&to=" + str(location_currency_code) + "&meta=ei%3Db-INVuGzDsy60gSThqFg"
        # returns the information provided by the given url
        result = web_utility.load_page(url)
        # initial shortening of result
        strip_result = (result[result.index('result'):])
        parts = strip_result.split(">")
        split_parts = parts[2].split(" ")
        result = float(split_parts[0])
    except:
        # General except clause to catch all error types
        result = -1
    return result


def get_details(country_name):
    # open currency_details.txt file in read only mode
    currency_details = open("currency_details.txt", mode="r", encoding="utf-8")

    for line in currency_details.readlines():
        parts = line.strip().split(",")
        if parts[0] == country_name:
            country_details_ea = tuple(parts)
            currency_details.close()
            return country_details_ea
    currency_details.close()
    return ()


# Testing
def main():
    print("Check convert")
    print("invalid Conversion           " + str(1.00) + "       AUD -> AUD   " + str(convert(1.00, "AUD", "AUD")))
    print("invalid Conversion           " + str(1.00) + "       JPY -> ABC   " + str(convert(1.00, "JPY", "ABC")))
    print("invalid Conversion           " + str(1.00) + "       ABC -> USD   " + str(convert(1.00, "ABC", "USD")))
    print("Valid Conversion             " + str(10.95) + "      AUD -> JPY   " + str(convert(10.95, "JPY", "AUD")))
    print("Valid Reversed Conversion    " + str(943.18) + "     JPY -> AUD   " + str(convert(943.18, "JPY", "AUD")))
    print("Valid Conversion             " + str(10.95) + "      AUD -> BGN   " + str(convert(10.95, "AUD", "BGN")))
    print("Valid Reversed Conversion    " + str(13.62) + "      BGN -> AUD   " + str(convert(13.62, "BGN", "AUD")))
    print("Valid Conversion             " + str(200.15) + "     BGN -> JPY   " + str(convert(200.15, "BGN", "JPY")))
    print("Valid Reversed Conversion    " + str(13589.49) + "   JPY -> BGN   " + str(convert(13589.49, "JPY", "BGN")))
    print("Valid Conversion             " + str(100.00) + "      JPY -> USD   " + str(convert(100.00, "JPY", "USD")))
    print("Valid Reversed Conversion    " + str(0.83) + "       USD -> JPY   " + str(convert(0.83, "USD", "JPY")))
    print("Valid Conversion             " + str(19.99) + "      USD -> BGN   " + str(convert(19.99, "USD", "BGN")))
    print("Valid Reversed Conversion    " + str(34.58) + "      BGN -> USD   " + str(convert(34.58, "BGN", "USD")))
    print("Valid Conversion             " + str(19.99) + "      USD -> AUD   " + str(convert(19.99, "USD", "AUD")))
    print("Valid Reversed Conversion    " + str(27.80) + "       AUD -> USD   " + str(convert(27.80, "USD", "AUD")))
    print("\nCheck get_details")
    print("invalid details              " + "Unknown     " + str(get_details("Unknown")))
    print("invalid details              " + "Japanese    " + str(get_details("Japanese")))
    print("invalid details              " + "            " + str(get_details("")))
    print("Valid details                " + "Australia   " + str(get_details("Australia")))
    print("Valid details                " + "Japan       " + str(get_details("Japan")))
    print("Valid details                " + "Hong Kong   " + str(get_details("Hong Kong")))
if __name__ == "__main__":
    main()
