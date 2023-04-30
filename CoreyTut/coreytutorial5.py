# Tutorial 5 https://www.youtube.com/watch?v=daefaLgNkw0
# Dictionaries

# key-value pairs

# student using dictionary

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}  # 'key': value; value can be list, string, float.. any mutable type. key can be str or int.

print(student['name'])  # specify needed key
print(student['courses'])

print(student.get('name'))
print(student.get('phone'))  # get returns None instead of an error, which previous method would give.

print(student.get('phone', 'Not Found'))  # custom response

student['phone'] = '555-5555'  # Set new key or update key

print(student)

student['name'] = 'Jane'
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5553'})  # takes a dictionary to update as an argument

print(student)

del student['age']  # deletes a key
phone = student.pop('phone')  # pops a key
print(phone)

student.update({'age': 26, 'phone': '555-5553'})

print(student)

print(len(student))  # length of dictionary

print(student.keys())  # list of keys
print(student.values())  # list of values
print(student.items())  # both

# you cannot directly loop through dictionaries for values, it will assume keys

for k in student:
	print(k)

for k, v in student.items():
	print(k, v)
for b in student.values():
	print(b)
