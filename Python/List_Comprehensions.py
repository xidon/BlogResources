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

A list comprehension can be broken down as:
"""
# [expression for element in iterator]

"""
This is the same as below for your standard for loop:
"""
# for element in iterator:
#     expression

"""
Here is a simple example of a standard for loop to square numbers in a range:
"""

squares = []

for x in range(4):
    squares.append(x**2)

print(squares)
# [0, 1, 4, 9]

"""
And this is the equivalent as a list comprehension:
"""

lc_squares = [x**2 for x in range(4)]

print(lc_squares)
# [0, 1, 4, 9]

"""
You could also have written it as a lambda function if you wanted to.
"""

lambda_squares = list(map(lambda x: x**2, range(4)))

print(lambda_squares)
# [0, 1, 4, 9]

"""
You will find that it is often easier to read a list comp than a lambda.

The variable x used in the for loop from the beginning will still exist 
after the loop has finished, while the other two ways won't leave this 
variable floating around.
"""


# If Else Conditions?  ----------------------


"""
You can use if else conditions in list comps.
Since the list comp is just each statement of a loop writen in order after
the expression we can easily understand how to lay this out.

Here is an example checking if a number in a list is even.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)

print(even)
# [2, 4, 6, 8, 10]

"""
And the list comp:
"""

lc_even = [n for n in numbers if n % 2 == 0]
print(lc_even)
# [2, 4, 6, 8, 10]

"""
You can start to see how readable and clean list comps can be.
Let's look at one with an else clause telling us that they odd numbers are
not even.
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
What happened there? If you noticed, now that the else clause has been
introduced the entire if else check is shifted at the start. This I suppose
is because depending on the results of the condition, the expression will be
different, and we know that the expression comes first in a list comp.
An if condition with no else only has one expression so the if can trail
after the for loop.
"""


# Nested For Loops?  ----------------------


"""
We are not limited to single loops with list comps. We can have nested loops
of various complexity. Below is a break down of the syntax.

For loop:
"""

# for a in iter_a:
#     for b in iter_b:
#         expression using a and b

"""
List comp:
"""

# [expression using a and b for a in iter_a for b in iter_b]

"""
Here is an example pairing two elements from two different lists:
"""

f_names = ["image_01", "image_02", "image_03"]
f_types = [".jpg", ".png"]

files = []
for f_name in f_names:
    for f_type in f_types:
        files.append(f_name + f_type)

print(files)
# ['image_01.jpg', 'image_01.png',
# 'image_02.jpg', 'image_02.png',
# 'image_03.jpg', 'image_03.png']

"""
The list comp version would be the expression first,
f_name + f_type followed by the for loops in the order they 
appear, for f_name in f_names then for f_type in f_types.

"""

lc_files = [f_name + f_type for f_name in f_names for f_type in f_types]

print(lc_files)
# ['image_01.jpg', 'image_01.png',
# 'image_02.jpg', 'image_02.png',
# 'image_03.jpg', 'image_03.png']

"""
Here is another example showing how to flatten a list of lists.
"""

numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_numbers = []

for l in numbers:
    for n in l:
        flat_numbers.append(n)

print(flat_numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

lc_flat_numbers = [n for l in numbers for n in l]
print(lc_flat_numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
Now lets say we need to return a list of lists, like in
this example of multiplying a matrix by a vector.
"""

matrix = [[5, 1, 3], [1, 1, 1], [1, 2, 1]]
vector = [1, 2, 3]
matrix_mult = []

for x in matrix:
    temp_list = []
    for z in range(len(x)):
        temp_list.append(x[z] * vector[z])
    matrix_mult.append(temp_list)

print(matrix)
print(matrix_mult)
# [[5, 1, 3], [1, 1, 1], [1, 2, 1]]
# [[5, 2, 9], [1, 2, 3], [1, 4, 3]]

"""
Unlike the flat numbers where we iterate through making one list, the matrix
is a list of 3 lists with 3 elements each.
So we need to construct and inner set of lists and return a list of those
lists. Although in a quick glance it looks like a nested for loop like before,
it is handled a little more different.

It is broken down from the inside out working on creating the temp_list and
adding that list to matrix_mult.

Lets see this as a for loop with and inner list comp
"""

matrix = [[5, 1, 3], [1, 1, 1], [1, 2, 1]]
vector = [1, 2, 3]
new_matrix_mult = []

for x in matrix:
    new_matrix_mult.append([x[z] * vector[z] for z in range(len(x))])

print(matrix_mult)
# [[5, 2, 9], [1, 2, 3], [1, 4, 3]]

"""
So as you can see from the inner for loop being taken care of with a list
comp, you can this of this not as a for loop nested inside another creating a
single list, but actually as a for loop creating a list using a nested for
loop that creates it's own list.

Now let's see the whole thing as a single list comp:
"""

matrix = [[5, 1, 3], [1, 1, 1], [1, 2, 1]]
vector = [1, 2, 3]

lc_matrix_mult = [[x[z] * vector[z] for z in range(len(x))] for x in matrix]
print(lc_matrix_mult)
# [[5, 2, 9], [1, 2, 3], [1, 4, 3]]

"""
Firstly let's take some time to appreciate that we have reduced 6 lines of
code down to a single line of code. Now let's break this beast down. So we
work from the inside out:

Our first list is [x[z] * vector[z] for z in range(len(x))] this is still
[expr for element in list]. Now for our outer list comp.
[[] for x in matrix] which is also [expr for element in list].
Nested together it looks like this:
"""
# [[expr for element in list] for element in list]
"""
In cases like this where the list comp is starting to get quite large, you
really have to start thinking about readability. I will let you decide which
level of complexity is your preferred. You may also look at using in-built
functions where possible.

Here is an example of a list comp vs an in-built function for transposing
rows and columns in a 3 x 4 matrix.
"""
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
print(transposed_matrix)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

"""
Or using the zip() function.
"""

zip_transposed_matrix = list(zip(*matrix))
print(zip_transposed_matrix)
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]


# Using Elif In List Comps  ----------------------


"""
If you want to have and elif statement in your conditionals then you are fat
out of luck as list comps don't support them. But lucky for you we have a
workaround.
If below...
"""
# if something:
#     expr
# elif some other thing:
#     expr
# else:
#     expr
"""
... is the same as below...
"""
# if something:
#     expr
# else:
#     if some other thing:
#         expr
#     else:
#         expr
"""
.. we can put it into a list comp.
The syntax is as follows:"""
# [expr if 1st cond.. else expr if 2nd cond.. else expr for elem in iterator]
"""Let's see and example, where I document if a number is odd or even.
I will do the normal for loop first then the list comp. I will write the for
loop in the same fashion that the list comp will be. That is to say avoiding
the use of an elif clause. The example below is for showcasing the syntax, as
in the real world this is quite and unruly line of code.
"""

numbers = [-3, -2, -1, 0, 1, 2, 3]

odd_evens = []
for n in numbers:
    if n == 0:
        odd_evens.append("0")
    else:
        if n % 2 == 0:
            odd_evens.append(str(n) + ": even")
        else:
            odd_evens.append(str(n) + ": odd")

print(odd_evens)
# ['-3: odd', '-2: even', '-1: odd', '0', '1: odd', '2: even', '3: odd']

lc_odd_evens = ["0" if n == 0
                else str(n) + ": even" if n % 2 == 0
                else str(n) + ": odd" for n in numbers]
print(lc_odd_evens)
# ['-3: odd', '-2: even', '-1: odd', '0', '1: odd', '2: even', '3: odd']

"""
I split the list comp over three lines. This adds to it's readability and fits
within standard line lengths.
With these line splits it does start to make you feel that you should have
just written a simple for loop with some if, elif, else statements.
"""

# END  ----------------------


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

# one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# two = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# sets = [(x, y) for x in one for y in two if x % 2 == 0 and y % 2 == 0]
# print(sets)
#
# crazy_sets = [(x, y) if x % 2 == 0 and y % 2 == 0 else (x, y) if x % 3 == 0 and y % 3 == 0 else "N/A" for x in one for y in two]
# print(crazy_sets)
#
# old_school_crazy = []
# for x in one:
#     for y in two:
#         if x % 2 == 0 and y % 2 == 0:
#             old_school_crazy.append((x, y))
#         elif x % 3 == 0 and y % 3 == 0:
#             old_school_crazy.append((x, y))
#         else:
#             old_school_crazy.append("N/A")
#
# print(old_school_crazy)
