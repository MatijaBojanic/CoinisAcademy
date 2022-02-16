# For an inputed side length, calculate rectangle perimeter and area
class rectangle:
    def __init__(self, first_side_length, second_side_length):
        self.first_side_length = first_side_length
        self.second_side_length = second_side_length
    def calculate_perimeter(self):
        return 2 * (self.first_side_length + self.second_side_length)
    def calculate_area(self):
        return self.first_side_length * self.second_side_length

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

square = rectangle(input_int_value("Input rectangle first side length"),input_int_value("Input rectangle second side length") )
print(square.calculate_perimeter())
print(square.calculate_area())