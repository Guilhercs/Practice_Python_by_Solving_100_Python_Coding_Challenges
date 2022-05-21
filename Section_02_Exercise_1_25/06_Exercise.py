"""
Exercise No. 6

Write a function that returns the string "something" joined with a space " " and the give argument a.

Examples

give_me_something("is better than nothing") -> "something is better than nothing"

given_me_something("Bob Jone") -> "something Bob Jone"

given_me_something("something") -> "something something"

Notes

Assume an input is give
"""


def give_me_something(a):
    return "something " + a


print(give_me_something("oi"))

#need a input

a = input("digit txt: ")
def give_me_something(a):
  return "something " + a

print(give_me_something(a))
