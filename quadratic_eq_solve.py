import cmath  
"""
According to maths formula's 
standard eq-> ax^2+bx=c=0
discriminate- d= (b^2-4*a*c)
solutions are:
alpha=(-b+root(d))/(2*a)
beta=(-b-root(d))/(2*a)

According to this the below code has been written
Generally the code displays fractional form of alpha and unit as beta.
"""
a = float(input('Enter coefficient of x^2: '))  
b = float(input('Enter coefficient of x: '))  
c = float(input('Enter constant: '))  
  
# calculate the discriminant  
d = (b**2) - (4*a*c)  
  
# find two solutions  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))