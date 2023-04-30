# Tutorial 4 https://www.youtube.com/watch?v=W8KRzm-HUcc
# Lists, Tuples, and Sets

courses = ['History', 'Math', 'Physics', 'CompSci']  # Values, CSV

print(courses)

print(len(courses))  # Length, number of items

print(courses[0])  # Index, as before, starts at 0

print(courses[-1])  # Negatives just loop around! But not positive items! Last item is always -1

print(courses[0:2])  # As before, a range, first is inclusive, second is NOT

print(courses[:2])  # Again, you can omit the first if it is 1

print(courses[2:])  # Or leave out the last one

# https://youtu.be/ajrtAuDg3yw Slicing Video

courses.append('Art')  # To add an item

print(courses)

courses.insert(0, 'Sports')  # To add an item at a specific index

print(courses)

courses.remove('Sports')  # Removes an item, only a single item
courses.remove('Art')
print(courses)
courses_2 = ['Art', 'Education']

# Extend adds multiple values

courses.insert(0, courses_2)  # Adds the list as an item, instead of adding the items in the list

print(courses)

del courses[0]  # Removes the item in the indexed position, only 1

courses.extend(courses_2)  # adds elements of courses_2 to courses

print(courses)

popped = courses.pop()  # If there's no argument, removes the last item. Also returns it, so can be used in definitions. Still pops it!

print(popped)

courses.pop()

print(courses)

courses.reverse()  # reverses orders

print(courses)

nums = [1, 5, 2, 4, 3]

courses.sort()  # Alphabetical/Ascending Order
nums.sort()

print(nums)
print(courses)

nums.sort(reverse=True)  # In reverse order
courses.sort(reverse=True)

print(nums)
print(courses)

# If you don't want to actually change the list, use the sorted function

courses = ['History', 'Math', 'Physics', 'CompSci']

sorted(courses)

print(courses)  # is not sorted
print(sorted(courses))

nums = [1, 5, 2, 4, 3]

print(min(nums))  # minimum
print(max(nums))  # maximum
print(sum(nums))  # sum


print(courses.index('CompSci'))  # Where CompSci was indexed in the list

print('CompSci' in courses)  # if 'CompSci' is in courses, boolean

# LOOP ---------------------------------------------
# Loops are marked by indentation
print('break')

for i2tem in courses:  # i2tem can be anything
	print(i2tem)

for index, course in enumerate(courses):  # enumerate returns index, course
	print(index, course)


for index, course in enumerate(courses, start=1):  # what the indices should start with, NOT the index to start listing with!
	print(index, course)

# Functionally equivalent to
for index, course in enumerate(courses):
	print(index + 1, course)

# Convert list into a string, separated by something

course_str = ', '.join(courses)  # 'Separator'.join()

print(course_str)

course_str = ' - '.join(courses)

print(course_str)
# The reverse, split a string along a certain value

new_list = course_str.split(' - ')

print(new_list)

# TUPLES --------------------------------------------------------------------
# tuples cannot be modified
print('break')

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

list_1[0] = 'Art'

print(list_2)  # list_2 is tied to list 1. You modify list_1 later, list_2 also inherits those modifications

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')  # Parentheses, not square brackets
tuple_2 = tuple_1

# tuple_1[0] = 'Art' # Will not work, as tuples are immutable 'TypeError: 'tuple' object does not support item assignment'

# They otherwise work just like lists. Just can't be modified.


# SETS ----------------------------------------------------------------------
# unordered, without duplicates

cs_courses = {'History', 'Math', 'Math', 'Physics', 'CompSci'}  # Curly braces, ignores duplicates

print(cs_courses)  # Order changes per execution!


# Membership tests--if a value is in a set. Sets are better than lists and tuples for this

print('Math' in cs_courses)

# Can also compare values, intersection, etc.

art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))  # intersection
print(cs_courses.difference(art_courses))  # difference
print(cs_courses.union(art_courses))  # union

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
# empty_set = {} # This isn't right! It's a dictionary
empty_set = set()
