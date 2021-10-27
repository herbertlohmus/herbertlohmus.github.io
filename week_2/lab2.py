import math


def factorial(n):
    '''
    Return the factorial of n.
    Recall that the factorial of n is defined to be: 1*2*3*...*(n-1)*n
    HINT:
    Use a for loop from 1 to n.
    On each iteration, multiply the current result by the current iteration number.
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    >>> factorial(10)
    3628800
    >>> factorial(100)
    93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    '''
    if n == 1:
        return n
    else:
        return n*factorial(n-1)


def is_prime(n):
    '''
    Return True if n is prime, and False otherwise.
    Recall that a prime number is divisible only by itself and 1,
    and by convention 1 is not considered to be a prime number.
    HINT:
    Use a for loop to check if every number between 2 and n-1 divides n
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(97)
    True
    >>> is_prime(99)
    False
    '''
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False


def num_digits(n):
    '''
    Return the number of digits in the input n.
    NOTE:
    A negative sign does not count as a digit,
    only numbers do.
    HINT:
    Use a while loop.
    In each iteration, divide the number by 10 to reduce the number of digits by 1.
    >>> num_digits(5)
    1
    >>> num_digits(10)
    2
    >>> num_digits(45678)
    5
    >>> num_digits(123456789012345678901234567890)
    30
    >>> num_digits(-5)
    1
    >>> num_digits(-10)
    2
    '''
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count


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

    if n >= 0:
        for i in range(0, n+1):
            if i*i == n:
                return True
            else:
                return False
    else:
        return False
