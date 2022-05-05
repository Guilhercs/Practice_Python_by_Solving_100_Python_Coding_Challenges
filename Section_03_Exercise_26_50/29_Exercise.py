"""
Exercise No. 29

Write a function that inverts the keys and values of a dictionary.

Examples:
     invert({'z': 'q', 'w': 'f'}) -> {'q': 'z', 'f': 'w'}

     invert({'a': 1, 'b': 2, 'c': 3}) -> {1: 'a', 2: 'b', 3: 'c'}

     invert({'zebra': 'koala', 'horse': 'camel'}) -> {'koala': 'zebra', 'camel': 'horse'}
"""


def invert(n):
    return {v: k for k, v in n.items()}


print(invert({'z': 'q', 'w': 'f'}))
