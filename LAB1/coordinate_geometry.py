import math

x1=int(input('Enter first x1 coordinate'))
y1=int(input('Enter first y1 coordinate'))
x2=int(input('Enter second x2 coordinate'))
y2=int(input('Enter second y2 coordinate'))

a=(x2 - x1)**2
b=(y2 - y1)**2
distance=(a+b)**0.5
print(distance)