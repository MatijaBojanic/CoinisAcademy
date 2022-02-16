# Swap first and last digit

def swap_first_and_last_digit(number):
    if number >= 10 or number <= -10:
        last_digit = str(number)[-1]
        if(number > 0):
            first_digit = str(number)[0]
            str_number = str(number)[1:-1]
            sign = '+'
        elif(number < 0):
            first_digit = str(number)[1]
            str_number = str(number)[2:-1]
            sign = '-'

        number = int(str(sign + last_digit + str_number + first_digit))

        return number
    else:
        return number

def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            return int_value
        except ValueError:
            print("Inputted value is not an integer")

number = input_int_value('Input the number')
print(swap_first_and_last_digit(number))