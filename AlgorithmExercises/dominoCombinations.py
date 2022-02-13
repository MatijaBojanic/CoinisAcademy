# Dominoes are  rectangular tiles with a line dividing its face into two square ends. Each end is marked with a number
# of spots or is blank. The maximum number of dots on a domino is decided the set size. Each combination is of numbers
# is unique.
# For an inputted number N,  1 <= N <= 1000, representing the maximum number in a domino set, find the sum of all dots.
# For N = 2 expected result is 12
# For N = 3 expected result is 30
# For N = 15 expected result is 2040
#
# Here I use two different approaches, mathematical and brute force

def print_math_and_brute_solution():
# Lets look at a domino set. For N = 1 we have 0-0, 1-0, 1-1
# for N = 2 we have 0-0, 1-0, 1-1, 2-0, 2-1, 2-2
# We are going to split the number of dots into left and right sums.
# Left sum is 0 + (1 + 1) + (2 + 2 + 2)
# Left sum is sum of n * (n + 1), for n = 0 to n = N
# Right sum is 0 + (0 + 1) + (0 + 1 + 2)
# Right sum is sum of sums for 0 to x, x = 0 to x = N
    max_number = max_dominoes_number_in_set()
    find_sum_of_all_dominoes_dots_math_version(max_number)
    find_sum_of_all_dominoes_dots_brute_force(max_number)

def find_sum_of_all_dominoes_dots_math_version(max_number):
    total_value = find_left_sum_for_dominoes_math(max_number) + find_right_sum_for_dominoes_math(max_number)
    print(total_value)

def find_sum_of_all_dominoes_dots_brute_force(max_number):
    total_value = find_left_sum_for_dominoes_brute(max_number) + find_right_sum_for_dominoes_brute(max_number)
    print(total_value)

def find_left_sum_for_dominoes_math(max_number):
    return max_number * (max_number + 1) * (max_number + 2) // 3

def find_right_sum_for_dominoes_math(max_number):
    return max_number * (max_number + 1) * (max_number + 2) // 6


def find_left_sum_for_dominoes_brute(max_number):
    left_sum = 0
    for x in range(max_number + 1):
        left_sum += x * (x + 1)
    return left_sum

def find_right_sum_for_dominoes_brute(max_number):
    right_sum = 0
    for x in range(max_number + 1):
        for j in range(x + 1):
            right_sum += j
    return right_sum

def max_dominoes_number_in_set():
# Checks if the number is less then 1 or more than 1000
    while True:
        inputted_number = input_int_value("Input a the maximum number on the dominoes")
        if inputted_number < 1 or inputted_number > 1000:
            print("Inputted value is not a is less then 1 or more then 1000. Input another number.")
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

print_math_and_brute_solution()









