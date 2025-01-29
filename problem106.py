#-------------------------------------------------------------
# Agata Holt
# Problem #106
# Problem106.py
#-------------------------------------------------------------
import sys
import numpy

#-------------------------------------------------------------
#main 
x=int(input("Enter x: ")) #input x
y=int(input("Enter y: ")) #input y

print ("The sum of x and y=", ( x + y)) #print the sum
print ("The difference of x and y=", ( x - y)) #print the difference
print ("The multiplication between x and y=", ( x * y))   #print the multiplication
print ("The division of x and y=", ( x / y))  #print the float result from this division
print ("The division of x and y=", ( x // y)) #rounds down to the nearest integer from this division
print ("The rest of the divion between x and y=", ( x % y))  #prints the  remainder of dividing

sys.exit (0)
