# find numbers divisible by 7 but not by 5 betwee 2000 and 3200

found_numbers = ""

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        found_numbers = found_numbers + (str(i) + ", ")

print(found_numbers)

# find factorial of given number from console input

# print("what number would you like to factorialize?")

to_factorial = int(input("what number would you like to factorialize?"))
factorial = 1

if to_factorial == 0:
    print(1)
else:
    for i in range(1, to_factorial + 1):
        factorial = factorial * i

print(factorial)

# integral number dictionary

to_integral = int(input("What number would you like to turn into an integral dictionary?"))
integral = {}

for i in range(1, to_integral + 1):
    integral[i] = i * i

print(integral)

# list and tuple from comma separated input numbers

to_list_tuple = input("Please enter a series of numbers separated by commas")

retrieved_list = to_list_tuple.split(", ")
retrieved_tuple = tuple(retrieved_list)

print(retrieved_list)
print(retrieved_tuple)


# class with input and output methods

class StringInputOutput:
    def __init__(self):
        self.classString = ""

    def getString(self):
        self.classString = input("please enter a string")

    def printString(self):
        print(self.classString)


class_test = StringInputOutput()

class_test.getString()
class_test.printString()
