#!/usr/bin/python3

# Author:   Benjamin Parry
# Blog:     benjamin.parry.com
# Post:     Python's Function Decorators
# Link:     http://benjamin-parry.com/2018/02/21/python-function-decorators


# Extending Functions With Functions ----------------------


def hello():
    def world():
        return "world."
    return "Hello " + world()
print(hello())

# Hello world.


def extended_greeting(func):
    return '{}, how are you?'.format(func[:-1])


def greeting(name):
    return 'Hello {}.'.format(name)

print(greeting('John'))
print(extended_greeting(greeting('John')))

# Hello John.
# Hello John, how are you?


# Extending Functions With Decorators ----------------------


def extended_greeting(func):
    def return_this_function(name):
        return '{}, how are you?'.format(func(name)[:-1])
    return return_this_function


@extended_greeting
def greeting(name):
    return 'Hello {}.'.format(name)

print(greeting('John'))

# Hello John, how are you?

greeting = extended_greeting(greeting('John'))


# Stacking Decorators ----------------------


def response(func):
    def wrapper(*args):
        return ("Users' response: " +
                input(func(*args)) +
                "\nThat's good.")
    return wrapper


def extended_greeting(func):
    def return_this_function(*args):
        return '{}, how are you?\n'.format(func(*args)[:-1])
    return return_this_function


@response
@extended_greeting
def greeting(name):
    return 'Hello {}.'.format(name)

print(greeting('John'))

# Hello John, how are you?
# >>> User types answer here
# Users' response: User's answer from above.
# That's Good.

greeting = response(extended_greeting(greeting('John')))


# Decorators With Arguments ----------------------


def response(friendly=True):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            if friendly:
                return ("Users' response: " +
                        input(func(*args, **kwargs)) +
                        "\nThat's good.")
            else:
                return ("Users response: " +
                        input(func(*args, **kwargs)) +
                        "\nHmmph, I really don't care.")
        return wrapper
    return real_decorator


def extended_greeting(func):
    def return_this_function(*args, **kwargs):
        return '{}, how are you?\n'.format(func(*args, **kwargs)[:-1])
    return return_this_function


@response(friendly=False)
@extended_greeting
def greeting(name):
    return 'Hello {}.'.format(name)

print(greeting('John'))

# Hello John, how are you?
# >>> User types answer here from above.
# Users' response: User's answer
# Hmmph, I really don't care.


# Recap ----------------------


# def decorator(arguments):
#     def real_decorator(function):
#         def wrapper(*args, **kwargs):
#             # code
#             # something_using_argument(arguments)
#             function(*args, **kwargs)
#             # more_code
#         return wrapper
#     return real_decorator
#
#
# @decorator(arguments)
# def function(*args, **kwargs):
#     return code
