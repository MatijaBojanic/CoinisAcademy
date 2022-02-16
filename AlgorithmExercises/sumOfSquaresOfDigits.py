# For a given 4 digit number, print the sum of squares of digits
def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            return int_value
        except ValueError:
            print("Inputted value is not an integer")
def input_four_digit():
    while True:
        four_digit_number = input_int_value('Input a 4 digit number')
        if four_digit_number >= 1000 and four_digit_number < 10000:
            return four_digit_number
        else:
            print('Inputed number is not a four digit number')
def sum_squares_of_digits(number):
    sum = 0
    number = abs(number)
    while number > 0:
        digit = number % 10
        sum += digit * digit
        number = number // 10
    return sum

four_digit_number = input_four_digit()
print(sum_squares_of_digits(four_digit_number))