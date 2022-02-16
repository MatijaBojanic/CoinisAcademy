# For an inputted radius, calculate circle perimeter and area
import math
class circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    def calculate_area(self):
        return self.radius * self.radius * math.pi

def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            if (int_value > 0):
                return int_value
            else:
                print("Value must be greater than zero")
        except ValueError:
            print("Inputted value is not an integer")

circle = circle(input_int_value("Input circle side length"))
print(circle.calculate_perimeter())
print(circle.calculate_area())