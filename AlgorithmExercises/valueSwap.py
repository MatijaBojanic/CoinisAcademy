# Switch the values of two inputted variables


def value_swap(first_value, second_value):
    first_value, second_value = second_value, first_value
    return first_value, second_value


first_value = input("Input the first variable \n")
second_value = input("Input the second variable \n")
first_value, second_value = value_swap(first_value, second_value)
print(first_value)
print(second_value)
