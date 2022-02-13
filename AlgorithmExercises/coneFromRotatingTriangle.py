import math
# Calculate the volume and surface area of a cone that is generated by rotating a triangle around its smaller leg

def calculate_volume_and_sa_of_cone():
# Calls both inputs and then calculates the volume
    first_leg = input_int_value("Input the value of the first leg")
    second_leg = input_int_value("Input the value of the second leg")
    print("Volume is: " + str(cone_volume(max(first_leg, second_leg), min(first_leg, second_leg))))
    print("Surface Area is: " + str(cone_surface_area(max(first_leg, second_leg), min(first_leg, second_leg))))
def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            if(int_value > 0):
                return int_value
            else:
                print("Value must be greater than zero")
        except ValueError:
            print("Inputted value is not an integer")

def cone_volume(height, radius):
    return math.pi * height * radius * radius * 1/3

def cone_surface_area(height, radius):
    return math.pi * radius * ( radius + math.sqrt(height * height + radius * radius))

calculate_volume_and_sa_of_cone()