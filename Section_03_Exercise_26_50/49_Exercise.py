"""
Exercise No. 49

Write a function that takes a list of lists and returns the value of all of the symbols in it, where each symbol adds or
takes something from the total score. Symbol values:
    - # = 5
    - O = 3
    - X = 1
    - ! = -1
    - !! = -3
    - !!! = -5

A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 -5) 8.
If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a x would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5
                                                                                     + 1) 3, so return 0.
Examples:
    check_score([
        ["#", "!"],
        ["!!", "X"]
    ]) -> 2

    check_score([
        ["!!!", "O", "!"],
        ["X", "#", "!!!"],
        ["!!", "X", "O"]
    ]) -> 0

    check_score([
        ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
        ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
        ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
        ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
        ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
        ["!!", "!!!" , "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
        ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#" "!!"],
        ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
        ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
        ["X", "!!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
        ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
        ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
        ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
        ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
    ]) -> 12

Notes:
    Strings in the list will only be #, O, X, !, !! and !!!.
"""

score = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}


def check_score(s):
    return max(0, sum(score[val] for row in s for val in row))


print(check_score([
        ["#", "!"],
        ["!!", "X"]
    ]))
