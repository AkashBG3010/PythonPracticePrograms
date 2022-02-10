import cmath

a = int(input("Enter the value of a: \n"))
b = int(input("Enter the value of b: \n"))
c = int(input("Enter the value of c: \n"))

delta = ((b*b) - (4*(a*c)))

eqn1 = (-b-cmath.sqrt(delta))/(2*a)
eqn2 = (-b+cmath.sqrt(delta))/(2*a)

print("The solution of Root_1 of X: ",eqn1)
print("The solution of Root_2 of X: ",eqn2)

print("----End of Program-----")