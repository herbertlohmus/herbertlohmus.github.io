'''
Anything between triple quote is a comment
'''
'''
# anything that begins with a hashtag is a comment
# comments are code that doesn't get executed
# print('hello world')
# print('goodbye world')
var1 = 'hello'
var2 = 'world'
var3 = var1 + ' ' + var2
print(var3)
# text is called a string
'''
'''
x = 1
y = 5
z = x * y + y (this is an expression)

# +-* are operators

python will always evaluate to a single value

# the type of number which doesn't have period is an "int" integer
# ** power operator 5**99 five to the power of 99
# non-integer numbers; (fractions, irrational numbers) are approximations
# type of number with a period is called a float or a floating point

# When a + is used on a string operator it is called a 'string concatenation'
    'herbert' + 'Lohmus' = herbertlohmus

# String * int = string replication

# python is an "untyped language" because we can change the type --> java is a typed language
print(z)
'''

# (a**2+- sqrt(b-4ac))/2a
'''
a = 5
b = 100
c = 2

quadratic1 = (a**2 + math.sqrt(b - 4 * a * c))/(2*a)
quadratic2 = (a**2 - math.sqrt(b - 4 * a * c))/(2*a)
print(quadratic1)
print(quadratic2)

a = 3

quadratic1 = (a**2 + math.sqrt(b - 4 * a * c))/(2*a)
quadratic2 = (a**2 - math.sqrt(b - 4 * a * c))/(2*a)

print(quadratic1)
print(quadratic2)


'''


'''
import math
def quadratic(a, b, c):
    result = (a**2 + math.sqrt(b - 4 * a * c))/(2*a)
    return result


print(quadratic(5, 100, 2))
# functions and variables are the key difference between python and CSS, HTML
'''
'''
print('Hello World!')

print('what is your name?')
myname = input()
print('It is good to meet you,' + myname)
print('the length of your name is:')
#len argument evaluates the length of a string argument into an integer
print(len(myname))

print('what is your age?')
myage = input()
print('you will be ' + str(int(myage)+1) + ' in a year.')
# int turn myage from a string to an int
# +1 added to the integer value of myage
# then the str function turns it into a sring from an integer

'''
# Boolean operators only have two values 'true' or 'false'

'''
Comparison operators

== equal to
!= not equal to
< less than
> greater than
<= less than or equal to
>= greater than or equal to

# strings and integers when compared will always return false
'''

'''
Boolean operators:
and, or, not

elif = else if

myage= 26
mypet = 'cat'
myage > 20 and mypet=="cat"
output: true

'''
'''
name = 'herbert'
if name == 'herbert':
    print('hi herbert')
print('done')
'''
'''
password = 'swordfish'
if password == 'swordfish':
    print('access granted')
else:
    print('wrong password')

x = 4%5
print (x)
'''
'''
Lab instructions:
Complete each function below so that all doctests pass.
Recall that you can run the doctests by running the command
$ python3 -m doctest --verbose lab.py
Once all doctests pass, upload the output of the above command to sakai.
NOTE:
Each problem should be relatively straightforward and take less than 10 minutes.
If you're spending more than 10 minutes on a problem,
then you should stop and seek help.
NOTE:
Your grade for all labs will be equal to max(0, 5 - number of failing test cases)
'''


def hypotenuse(a, b):
    '''
    Return the square root of a squared plus b squared.
    >>> hypotenuse(3.0, 4.0)
    5.0
    >>> hypotenuse(12.0, 5.0)
    13.0
    '''


def is_even(n):
    '''
    Return True if n is even and False if n is odd.
    HINT: Use the modulus operator %
    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2000)
    True
    >>> is_even(-8)
    True
    >>> is_even(-9)
    False
    '''


if n % 2 == 0
    return True
else
    return False


def is_odd(n):
    '''
    Return True if n is odd and False if n is even.
    >>> is_even(0)
    False
    >>> is_even(1)
    True
    >>> is_even(2000)
    False
    >>> is_even(-8)
    False
    >>> is_even(-9)
    True
    '''


def absolute_value(n):
    '''
    Return the absolute value of n.
    HINT:
    Use an if statement.
    >>> absolute_value(5)
    5
    >>> absolute_value(-5)
    5
    >>> absolute_value(5.5)
    5.5
    >>> absolute_value(-5.5)
    5.5
    '''


def max_num(a, b):
    '''
    Return the maximum of a and b.
    HINT:
    Use an if statement.
    >>> max_num(4, 5)
    5
    >>> max_num(5, 4)
    5
    >>> max_num(-4, -5)
    -4
    >>> max_num(4, 4)
    4
    '''


def max_num_4(a, b, c, d):
    '''
    Return the maximum of a, b, c, and d.
    HINT:
    Use many if statements.
    >>> max_num_4(1,2,3,4)
    4
    >>> max_num_4(2,3,4,1)
    4
    >>> max_num_4(3,4,1,2)
    4
    >>> max_num_4(4,1,2,3)
    4
    >>> max_num_4(10,1,2,3)
    10
    '''


def max_num_abs(a, b):
    '''
    Return the number with the highest absolute value.
    HINT:
    Use an if statement, but be careful about the condition.
    >>> max_num_abs(4,5)
    5
    >>> max_num_abs(4,5)
    5
    >>> max_num_abs(-4,-5)
    -5
    >>> max_num_abs(4,4)
    4
    '''


def is_leap_year(n):
    '''
    Return True if n is a leap year and False otherwise.
    HINT:
    You can find the formula to calculate leap years here at
    https://www.mathsisfun.com/leap-years.html
    >>> is_leap_year(1582)
    False
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2018)
    False
    >>> is_leap_year(2019)
    False
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(2200)
    False
    >>> is_leap_year(2400)
    True
    '''


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


def fibonacci(n):
    '''
    Return the nth fibonacci number.
    Recall that the fibonacci numbers are calculated by the following formula:
        fibonacci(0) = 0
        fibonacci(1) = 1
        fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    HINT:
    The following "pseudocode" describes how to calculate the nth fibonacci number:
    Let f0 = 0
    Let f1 = 1
    In a for loop from 0 to n,
        Let fn = f0 + f1
        Let f0 = f1
        Let f1 = fn
