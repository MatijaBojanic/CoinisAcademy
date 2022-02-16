#Check if the inputted year is a leap year or not

def is_leap_year():
    year = input_int_value("Input the year")
    if((year % 400 == 0) or  (year % 100 != 0) and  (year % 4 == 0)):
        print("Given year is a leap year");
    else:
        print ("Given year is not a leap year")

def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            return int_value
        except ValueError:
            print("Inputted value is not an integer")

is_leap_year()