import math


def is_perfect_square(n):
    '''
    Return True if n is is the product of two integers.
    That is, return True if there exists an integer i such that i*i==n.
    HINT:
    Use a for loop to check each number i between 0 and n.
    >>> is_perfect_square(1)
    True
    >>> is_perfect_square(2)
    False
    >>> is_perfect_square(4)
    True
    >>> is_perfect_square(81)
    True
    >>> is_perfect_square(97)
    False
    >>> is_perfect_square(0)
    True
    >>> is_perfect_square(-144)
    False
    >>> is_perfect_square(144)
    True
    '''

    if n >= 0 and (n**0.5) % 1 == 0:
        return True
    else:
        return False


'''
    root = math.sqrt(n)
    for i in range(n+1):
        if int(root + 0.5) ** 2 == n:
            return True
        else:
            return False
    else:
        return False
'''
"""
    if n >= 0:
        for i in range(n+1):
            if i*i == n:
                return True
            else:
                return False
    else:
        return False
"""
