#!/usr/bin/python3

# Author:   Benjamin Parry
# Blog:     benjamin.parry.com
# Post:     Python's List Comprehensions
# Link:     http://benjamin-parry.com/2018/03/07/list-comprehensions

for_list = []

for x in range(4):
    for_list.append(x*x)

print(for_list)
# [0, 1, 4, 9]

comps_list = [x*x for x in range(4)]

print(comps_list)
# [0, 1, 4, 9]

lambda_list = list(map(lambda x: x*x, range(4)))

print(lambda_list)
# [0, 1, 4, 9]

for_list = []

for x in "Monty":
    for i in range(1, 3):
        for_list.append(x*i)

print(for_list)

comps_list = [x*i for x in "Monty" for i in range(1, 3)]

print(comps_list)

import functools
what = list(str(functools.reduce(lambda x,y:x+y,map(lambda x:x**x,range(1, 50))))[-10:])

print(what)
one = map(lambda x:x**x,range(1, 10))
print(list(one))
two = str(functools.reduce(lambda x,y: x+y, map(lambda x:x**x,range(1, 10))))
print(two)

# what_comp = [[x + y for x, y in ] for]
