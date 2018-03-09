#!/usr/bin/python3

"""
Author:   Benjamin Parry
Blog:     benjamin.parry.com
Post:     Python's List Comprehensions
Link:     http://benjamin-parry.com/2018/03/07/python-list-comprehensions
"""


# What Are List Comprehensions?  ----------------------


"""
List comprehensions are inline for loops, wrapped inside square brackets, that
result in a new list.

For example a standard for loop to square a number in a range would be:
"""

sq_list = []

for x in range(4):
    sq_list.append(x**2)

print(sq_list)
# [0, 1, 4, 9]

"""
And this is the equivalent as a list comprehension:
"""

sq_l_comp = [x**2 for x in range(4)]

print(sq_l_comp)
# [0, 1, 4, 9]

"""
You could also have written it as a lambda function if you wanted to.
"""

sq_lambda = list(map(lambda x: x**2, range(4)))

print(sq_lambda)
# [0, 1, 4, 9]

"""
You will find that it is often easier to read a list comp than a lambda.

The variable x used in the for loop from the beginning will still exist 
after the loop has finished, while the other two ways won't leave this 
variable floating around.

A list comprehension can be broken down as [expression for item in iterator]

This is the same as below for your standard for loop:
"""

# for item in iterator:
#     expression

"""
We can go further with this and have nested for loops, too.
Here is a for loop:
"""

# for a in iter_a:
#     for b in iter_b:
#         expression using a and b

"""
And here is the same as a list comp:
"""

# [expression using a and b for a in iter_a for b in iter_b]

"""
Here is an example pairing two elements from two different lists:
"""

f_names = ["image_01", "image_02", "image_03"]
f_types = [".jpg", ".png"]

file_list = []
for f_name in f_names:
    for f_type in f_types:
        file_list.append(f_name + f_type)


print(file_list)
# ['image_01.jpg', 'image_01.png',
# 'image_02.jpg', 'image_02.png',
# 'image_03.jpg', 'image_03.png']

"""
The list comp verions would be the expression first,
f_name + f_type followed by the for loops in the order they 
apear, for f_name in f_names then for f_type in f_types.

"""

c_file_list = [f_name + f_type for f_name in f_names for f_type in f_types]

print(c_file_list)
# ['image_01.jpg', 'image_01.png',
# 'image_02.jpg', 'image_02.png',
# 'image_03.jpg', 'image_03.png']

"""
You can use if else conditions in list comps, too.
Since the list comp is jsut each statement of a loop writen in order after 
the expression we can easily understand how to lay this out.

Lets look at this with a simple check to see if a number is even.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)

print(even)
# [2, 4, 6, 8, 10]

"""
And as a list comp:
"""

lc_even = [n for n in numbers if n % 2 == 0]
print(lc_even)
# [2, 4, 6, 8, 10]

"""
You can start to see how readable and clean list comps can be.
Let's look at one with an else clause.
"""

numbers = [1, 2, 3, 4]
even = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        even.append(str(n) + " is not even")

print(even)
# ['1 is not even', 2, '3 is not even', 4]

lc_even = [n if n % 2 == 0 else str(n) + " is not even" for n in numbers]
print(lc_even)
# ['1 is not even', 2, '3 is not even', 4]

"""
Now that it different. If you noticed here, now that there is an else clause,
the entire if else check is shifted at the start.
"""

# i = 2
# while i < 20:
#     j = 2
#     while j <= (i//j):
#         if not(i % j):
#             break
#         j += 1
#     if j > (i//j):
#         pair_list.append("{} is prime".format(i))
#     i += 1
# print(pair_list)
# i = 2
#
# for i in range(2, 20):


# END  ----------------------


for_list = []

for x in "Monty":
    for i in range(1, 3):
        for_list.append(x*i)

print(for_list)

comps_list = [x*i for x in "Monty" for i in range(1, 3)]

print(comps_list)


matrix_x = [[5, 1, 3], [1, 1, 1], [1, 2, 1]]

my_vector = [1, 2, 3]
matrix_y_loop = []

for x in matrix_x:
    temp_list = []
    for z in range(len(x)):
        temp_list.append(x[z] * my_vector[z])
    matrix_y_loop.append(temp_list)

matrix_y = [[x[z] * my_vector[z] for z in range(len(x))] for x in matrix_x]

print(matrix_x)
print(matrix_y_loop)
print(matrix_y)

# import functools
# what = list(str(
#     functools.reduce(
#         lambda x,y:x+y,map(
#             lambda x:x**x,range(1, 50))))[-10:])
#
# print(what)
# one = map(lambda x:x**x,range(1, 10))
# print(list(one))
# two = str(functools.reduce(lambda x,y: x+y, map(lambda x:x**x,range(1, 10))))
# print(two)

# what_comp = [[x + y for x, y in ] for]


"""for x in range(10):

for i in range(10, 20):

new_list.append(x*i)

is the same as

new_list = [x*i for x in range(10) for i in range(10, 20)]

loops vs list comps

how to use them

generator comps

dict comps

List, generator, dict comps"""