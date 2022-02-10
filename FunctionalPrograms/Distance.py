import math

x = int(input("Enter the value of 'X' of point-1: \n"))     # Reading user input for x value in point(x,y)
y = int(input("Enter the value of 'Y' of point-1: \n"))     # Reading user input for y value in point(x,y)
print("Entered point is: (",x,",",y,")")        # printing the entered values

dist = math.sqrt((x*x) + (y*y))     # Distance calculation between the points

print("Distance from (",x,", ",y,") to (0, 0) = ",dist, "Unit(s)")      # Printing the distance as output

print("----End of Program-----")