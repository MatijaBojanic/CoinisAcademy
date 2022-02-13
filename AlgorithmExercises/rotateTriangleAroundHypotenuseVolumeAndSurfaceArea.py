import math
# Calculate the volume and surface area of a cone that is generated by rotating a right angle triangle around its hypotenuse
# The body generated in this way is a double-cone

def revolve_triangle_around_hypotenuse():
# Calls both inputs and then, finds the radius and  calculates the volume and surface area
    first_leg = input_int_value("Input the value of the first leg")
    second_leg = input_int_value("Input the value of the second leg")
    hypotenuse = math.sqrt(first_leg * first_leg + second_leg * second_leg)
    radius = find_radius(first_leg, second_leg, hypotenuse)
    print("Volume is: " + str(double_cone_volume(radius, hypotenuse)))
    print("Surface Area is: " + str(double_cone_surface_area(radius, first_leg, second_leg)))


def find_radius(first_leg, second_leg, hypotenuse):
    return first_leg * second_leg / hypotenuse

def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            if(int_value > 0):
                return int_value
            else:
                print("Value must be higher than zero")
        except ValueError:
            print("Inputted value is not an integer")

def double_cone_volume(radius, height):
    return math.pi * radius * radius * height


def double_cone_surface_area(radius, first_slant, second_slant):
    return math.pi * radius * ( first_slant + second_slant)

revolve_triangle_around_hypotenuse()