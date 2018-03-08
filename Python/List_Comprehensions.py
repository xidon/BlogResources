#!/usr/bin/python3

# Author:   Benjamin Parry
# Blog:     benjamin.parry.com
# Post:     Python's List Comprehensions
# Link:     http://benjamin-parry.com/2018/03/07/python-list-comprehensions

for_list = []

for x in range(4):
    for_list.append(x**2)

print(for_list)
# [0, 1, 4, 9]

comps_list = [x**2 for x in range(8)]

print(comps_list)
# [0, 1, 4, 9]

lambda_list = list(map(lambda x: x**2, range(11)))

print(lambda_list)
# [0, 1, 4, 9]

# for item in iterator:
#     expression

new_list = []
for item_a in iterator_a:
    for item_b in iterator_b:
        expression eg new_list.append(a*b)

for_list = []

for x in "Monty":
    for i in range(1, 3):
        for_list.append(x*i)

print(for_list)

comps_list = [x*i for x in "Monty" for i in range(1, 3)]

print(comps_list)

# import functools
# what = list(str(functools.reduce(lambda x,y:x+y,map(lambda x:x**x,range(1, 50))))[-10:])
#
# print(what)
# one = map(lambda x:x**x,range(1, 10))
# print(list(one))
# two = str(functools.reduce(lambda x,y: x+y, map(lambda x:x**x,range(1, 10))))
# print(two)

# what_comp = [[x + y for x, y in ] for]
