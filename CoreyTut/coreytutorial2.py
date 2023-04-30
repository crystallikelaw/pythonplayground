# Tutorial 2 https://www.youtube.com/watch?v=k9TUPpGqYTo
# Textual Data
# Python operates on whitespace

message = 'Hello World'  # Variable names are lowercase, underscores. Be descriptive! Double quotes can be used if the data contains '

message2 = 'Bobby\'s World'  # Escape
message3 = "Bobby's World"

print(message)
print(message2)
print(message3)

message4 = ''' Bobby\'s world is a good cartoon in the 1990\'s Bobby\'s world is a good cartoon in the 1990\'s Bobby\'s world is a good cartoon in the 1990\'s Bobby\'s world is a good cartoon in the 1990\'s'''  # Triple quotes for multiline messages

print(message4)


print(len(message))  # Length of the string

print(message[4])  # Index of position in string, starts at 0

print(message[0:5])  # Starting point : Ending point; first index is inclusive, second is NOT 0:5 is indices 0,1,2,3,4

print(message[:5])  # can omit the first

print(message[6:])  # or the last if we want the rest

#  This is 'slicing' https://youtu.be/ajrtAuDg3yw

# Method is a function that belongs to an object, interchangeable for now
# METHODS -------------------------------------------------------------------

print(message.lower())  # Lowercase
print(message.upper())  # Uppercase


print(message.count('Hello'))  # counts whatever its argument is, indicates that Hello appears in the string
print(message.count('l'))

print(message.find('World'))  # Returns starting index, -1 if it doesn't exist

message.replace('World', 'Universe')  # replaces, returns a string after, but doesn't overwrite message!

new_message = message.replace('World', 'Universe')


message = message.replace('World', 'Universe')  # This will actually replace the variable messages

print(new_message)
print(message)

greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name  # Plus sign joins strings. but no space. Comma and space are literal

print(message)

message = greeting + ', ' + name + '. Welcome!'

print(message)

# Formatted String

message = '{}, {}. Welcome back!'.format(greeting, name)  # {} is a placeholder. .format fills in placeholders.


print(message)

# Detailed string formatting video https://youtu.be/vTX3IwquFkc

# Python 3.6 or higher has fstrings

message = f'{greeting}, {name.upper()}. Welcome back home!'  # Fstrings are better. f goes OUTSIDE the leading '. You can add methods inside the {}

print(message)

print(dir(name))  # Will show all attributes/methods that are legal for the variable

print(help(str))  # More information

print(help(str.lower))  # Of just lower
