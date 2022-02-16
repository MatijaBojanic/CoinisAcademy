# For a three digit number and a two digit number as digits, calculate sum.

def input_number_as_digits(number_of_digits):
# If we are inputing a single digit number, the digit can be between -9 and 9 including 0
# If we are inputing a multi digit number, the first digit can be between -9 and 9 excluding 0
# The rest of the digits must be between 1 and 9
    number_str = ""
    current_digit = 0
    while current_digit < number_of_digits:
        if (number_of_digits == 1):
            digit = input_first_digit(current_digit)
        elif(number_of_digits > 1 and current_digit == 0):
            while True:
                digit = input_first_digit(current_digit)
                if(digit == 0):
                    print('First digit of a multi digit number can not be zero')
                else:
                    break
        elif(number_of_digits > 1 and current_digit > 0):
            digit = input_digit(current_digit)
        current_digit = current_digit + 1
        number_str = number_str + str(digit)
    return int(number_str)

def input_first_digit(current_digit):
    while True:
        digit = input_int_value("Input " + str(current_digit + 1) + ". digit")
        if (digit > -10 and digit < 10):
            return digit
        elif digit <= -10 or digit >= 10:
            print('Input a single digit')

def input_digit(current_digit):
    while True:
        digit = input_int_value("Input " + str(current_digit + 1) + ". digit")
        if (digit >= 0 and digit < 10):
            return digit
        elif digit >= 10:
            print('A digit can not be greater than 9')
        elif digit < 0:
            print('Only the first digit can have a negative value')

def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            return int_value
        except ValueError:
            print("Inputted value is not an integer")

three_digit_number = input_number_as_digits(3)
print("First number: " + str(three_digit_number))
two_digit_number = input_number_as_digits(2)
print("Second number: " + str(two_digit_number))
print(three_digit_number + two_digit_number)
