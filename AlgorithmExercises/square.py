# For an inputed side length, calculate square perimeter and area
class square:
    def __init__(self, side_length):
        self.side_length = side_length
    def calculate_perimeter(self):
        return 4 * self.side_length
    def calculate_area(self):
        return self.side_length * self.side_length

def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            return int_value
        except ValueError:
            print("Inputted value is not an integer")

square = square(input_int_value("Input square side length"))
print(square.calculate_perimeter())
print(square.calculate_area())