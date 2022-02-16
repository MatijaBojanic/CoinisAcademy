# For an inputted number 1-12, representing the month, and year, print number of days in the correct month

def is_leap_year(year):
    if((year % 400 == 0) or  (year % 100 != 0) and  (year % 4 == 0)):
        return True
    else:
        return False

def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            return int_value
        except ValueError:
            print("Inputted value is not an integer")

def month_input():
    while True:
        month_int = input_int_value('Input month integer (1-12)')
        if month_int < 13 and month_int > 0:
            return month_int
        else:
            print("Month must be in the range 1 to 12")

def num_of_days_in_month():
# We could avoid the second input unless the first one is equal to 2 (if its not february we dont need to check the year)
    month = month_input()
    year = input_int_value('Input year')
    if month in [1,3,5,7,8,10,12]:
        print("Month has 31 days")
    elif month in [4,5,9,11]:
        print("Month has 30 days")
    elif month == 2:
        if is_leap_year(year):
            print("Month has 29 days")
        else:
            print("Month has 28 days")

num_of_days_in_month()