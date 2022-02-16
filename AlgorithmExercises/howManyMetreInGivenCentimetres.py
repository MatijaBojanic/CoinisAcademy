# For given centimetre int print out how many metres are in it (324 cm => 3 m)
def metre_in_centimetre(centimetre):
    return centimetre // 100

def input_int_value(msg):
# Gets value, while throwing value errors
    while True:
        try:
            int_value = int(input(msg + "\n"))
            return int_value
        except ValueError:
            print("Inputted value is not an integer")

centimetre = input_int_value('Input centimetres')
print(metre_in_centimetre(centimetre))