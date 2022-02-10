import math

x = int(input("Enter the value of 'X' of point-1: \n"))
y = int(input("Enter the value of 'Y' of point-1: \n"))
print("Entered point is: (",x,",",y,")")

dist = math.sqrt((x*x) + (y*y))

print("distance from (",x,", ",y,") to (0, 0) = ",dist)

print("----End of Program-----")