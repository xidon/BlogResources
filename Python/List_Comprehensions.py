#!/usr/bin/python3

"""
Author:   Benjamin Parry
Blog:     benjamin.parry.com
Post:     Python's List Comprehensions
Link:     http://benjamin-parry.com/2018/03/11/python-list-comprehensions
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


# If Else Conditions.  ----------------------


"""
You can use if else conditions in list comps. Since the list comp is just
each statement of a loop written in order after the expression we can easily
understand how to lay this out.

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
        even.append(str(n) + ": odd")

print(even)
# ['1: odd', 2, '3: odd', 4]

lc_even = [n if n % 2 == 0 else str(n) + ": odd" for n in numbers]

print(lc_even)
# ['1: odd', 2, '3: odd', 4]

"""
What happened there? If you noticed, now that the else clause has been
introduced, the entire if else check is shifted to the start. This I suppose
is because depending on the results of the if else checks, the expression will
be different. We know already that the expression comes first in a list comp.
An if condition with no else only has one expression so the if can trail
after the for loop.
"""


# Nested For Loops.  ----------------------


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
f_formats = [".jpg", ".png"]

files = []
for f_name in f_names:
    for f_format in f_formats:
        files.append(f_name + f_format)

print(files)
# ['image_01.jpg', 'image_01.png',
# 'image_02.jpg', 'image_02.png',
# 'image_03.jpg', 'image_03.png']

"""
The list comp version would be the expression first,
f_name + f_format followed by the for loops in the order they
appear, for f_name in f_names then for f_format in f_formats.

"""

lc_files = [f_name + f_format for f_name in f_names for f_format in f_formats]

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


# A List Of Lists.  ----------------------


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
# [[5, 1, 3], [1, 1, 1], [1, 2, 1]]
print(matrix_mult)
# [[5, 2, 9], [1, 2, 3], [1, 4, 3]]

"""
Unlike the flat numbers where we iterate through making one list, the matrix
is a list of 3 lists with 3 elements each.
So we need to construct and inner set of lists and return a list of those
lists. Although in a quick glance it looks like a nested for loop like before,
it is handled a little more differently.

It is broken down from the inside out working on creating the temp_list and
adding that list to matrix_mult.

Lets first see this as a for loop with the inner loop as a list comp:
"""

matrix = [[5, 1, 3], [1, 1, 1], [1, 2, 1]]
vector = [1, 2, 3]
new_matrix_mult = []

for x in matrix:
    new_matrix_mult.append([x[z] * vector[z] for z in range(len(x))])

print(matrix_mult)
# [[5, 2, 9], [1, 2, 3], [1, 4, 3]]

"""
From making the inner for loop being taken care of with a list
comp, you can this of this not as a for loop nested inside another creating a
single list, but actually as a for loop creating a list using a nested for
loop that creates its own list.

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
[expr for element in list]. The outer list comp is [[] for x in matrix],
which is also [expr for element in list]. Nested together it looks like this:
"""
# [[expr for element in list] for element in list]


# Don't Go Overboard!  ----------------------


"""
In cases like above where the list comp is starting to get quite large, you
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
The zip() function:
"""

zip_transposed_matrix = list(zip(*matrix))
print(zip_transposed_matrix)
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

"""
You can see that the zip() function is less code and is quite a lot easier to
read.
"""


# Using Elif In List Comps.  ----------------------


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
We do this.
"""
# if something:
#     expr
# else:
#     if some other thing:
#         expr
#     else:
#         expr
"""
Now we can make a list comp.
The syntax is as follows:
"""
# [expr if 1st cond.. else expr if 2nd cond.. else expr for elem in iterator]
"""
Let's see an example, where I append odd or even to number but not to 0.

I'll show you a for loop first. It will be written excluding the use of elif,
to better understand the flow of the list comp. This is an example of a list
comp becoming too long, but it is useful to showcase the syntax.
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
I split the list comp over three lines. This adds to its readability and fits
within standard line lengths.
With these line splits it does start to make you feel that you should have
just written a simple for loop with some if, elif, else statements.
"""

# END  ----------------------
