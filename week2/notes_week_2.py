'''
Anything between triple quote is a comment
'''
'''
# anything that begins with a hashtag is a comment
# comments are code that doesn't get executed
#print('hello world')
#print('goodbye world')
var1 = 'hello'
var2 = 'world'
var3 = var1 + ' ' + var2
print(var3)
# text is called a string
'''
'''
x = 1
y = 5
z = x * y + y
# the type of number which doesn't have period is an int
# ** power operator 5**99 five to the power of 99
# non-integer numbers; (fractions, irrational numbers) are approximations
# type of number with a period is called a float

#python is an "untyped language" because we can change the type --> java is a typed language
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




import math
def quadratic(a, b, c):
    result = (a**2 + math.sqrt(b - 4 * a * c))/(2*a)
    return result


print(quadratic(5, 100, 2))
# functions and variables are the key difference between python and CSS, HTML
