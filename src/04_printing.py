"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
# %s is for strings
# %d is for intergers
print("x is %d , y is % f, z is '% s'" % (x, y, z))

# Use the 'format' string method to print the same thing
print("x is {ten}, y is {float}, z is '{turtles}'.format(ten=10, float=2.25, turtles='I like turtles!')")
# Finally, print the same thing using an f-string
y = 2.25
print(f"x is {x}, y is {y}, z is '{z}'")
