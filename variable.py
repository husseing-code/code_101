#Establish variables
a = 5
b = 6
c = 7

#Calculate the perimeter
s = (a + b + c) / 2

#Calcualte the area
area = (s*(s-a)*(s-b)*(s-c))**.5
print('The area of the triangle is %0.3f' % area)
