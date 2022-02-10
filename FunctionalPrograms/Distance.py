import math


def distanceCalculation(x, y):      # Function to perform the arithmetic operation
    dist = math.sqrt((x * x) + (y * y))  # Distance calculation between the points
    print("And it's distance from (", x, ", ", y, ") to (0, 0) = ", dist, "Unit(s)")  # Printing the distance as output


x = int(input("Enter the value of 'X' of point-1: \n"))     # Reading user input for x value in point(x,y)
y = int(input("Enter the value of 'Y' of point-1: \n"))     # Reading user input for y value in point(x,y)
print("Entered point is: (",x,",",y,")")        # printing the entered values
distanceCalculation(x,y)        # Function Calling


print("----End of Program-----")