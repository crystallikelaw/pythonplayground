# Tutorial 3 https://www.youtube.com/watch?v=khKv-8q7YmY
# Numeric Data


# Integer is a whole number, float is a decimal

num = 3

print(type(num))  # The type of the variable

print(help(type))


num = 3.14

print(type(num))

# OPERATORS -------------------------------------------------------------

# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)  # Floor division, drop decimal
print(3 ** 2)
print(3 % 2)  # Delivers remainder, can be used to tell if a number is even or odd

print((3 // 2) + (3 % 2) / 2)  # Definitionally true

print(5 % 2)
print(4 % 2)
print(3 % 2)
print(2 % 2)

print(3 * (2 + 1))

num = 1

num = num + 1  # incrementing values

print(num)

num += 1  # Shorthand for incrementing values

print(num)

num *= 10  # Works with other operators

print(num)

# FUNCTIONS -------------------------------------------------------------------

print(abs(-3))  # Absolute Value

print(round(3.75))  # Rounds the number

print(round(3.752, 1))  # Rounds the number to the 1 digit after the decimal

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

# Will return Booleans, ie. True/False

num1 = 3
num2 = 2
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)


num_1 = '100'  # These are set as strings
num_2 = '200'

print(num_1 + num_2)  # plus sign is combining strings

print(type(num_1))
# Casting is changing input type

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)
print(type(num_1))


num_1 = float(num_1)
print(type(num_1))
print(num_1 + num_2)
