import math
# Calculate the volume of cone that is generated by rotating a triangle around its smaller leg

def calculate_volume_of_cone():
# Calls both inputs and then calculates the volume
    first_leg = input_int_value("Input the value of the first leg")
    second_leg = input_int_value("Input the value of the second leg")
    print(cone_volume(max(first_leg, second_leg), min(first_leg, second_leg)))

def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            return int_value
        except ValueError:
            print("Inputted value is not an integer")

def cone_volume(height, radius):
    return math.pi * height * radius * radius * 1/3


calculate_volume_of_cone()