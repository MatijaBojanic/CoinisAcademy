# For two inputted integers print out if the first integer is divisible by the second integer


def check_if_number_is_divisible_by_another_number():
    first_number = input_int_value("Input the first integer")
    second_number = input_non_zero_int_value("Input the second integer")
    if first_number % second_number == 0:
        print(str(first_number) + " is divisible by " + str(second_number))
    else:
        print(str(first_number) + " is NOT divisible by " + str(second_number))

def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            return int_value
        except ValueError:
            print("Inputted value is not an integer")
def input_non_zero_int_value(msg):
    while True:
        non_zero_int = input_int_value(msg)
        if(non_zero_int != 0):
            return non_zero_int
        else:
            print("The integer must not be a zero")

check_if_number_is_divisible_by_another_number()