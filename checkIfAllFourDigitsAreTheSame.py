# For an inputed 4 digit number, print "Super" if all digits are equal

def print_super_if_all_digits_equal():
    number = input_four_digit_number()
    if all_digits_are_equal(number):
        print("Super")

def all_digits_are_equal(number):
# Checks if all numbers are equal. Returns bool.
    previous_number = None
    all_equal = True
    while number > 0:
        new_number = number % 10
        if previous_number != None and previous_number != new_number:
            all_equal = False
            break;
        previous_number = new_number
        number = number // 10
    return all_equal

def input_four_digit_number():
# Checks if value is a 4-digit number, if not requires another input. Returns the 4-digit number
    while True:
        inputted_number = input_int_value("Input a four digit integer")
        if inputted_number < 1000 or inputted_number > 9999:
            print("Inputted value is not a four digit integer")
        else:
            return inputted_number

def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            return int_value
        except ValueError:
            print("Inputted value is not an integer")



print_super_if_all_digits_equal()