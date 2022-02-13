# For two inputted integers print out if the first integer is divisible by the second integer


def check_if_number_is_divisible_by_another_number():
    first_number = input_int_value("Unesite prirodni broj")
    second_number = input_int_value("Unesite prirodni broj")
    if first_number % second_number == 0:
        print(str(first_number) + "is divisible by " + str(second_number))
    else:
        print(str(first_number) + "is NOT divisible by " + str(second_number))

def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            if(int_value > 0):
                return int_value
            else:
                print("Value must be more than zero")
        except ValueError:
            print("Inputted value is not an integer")