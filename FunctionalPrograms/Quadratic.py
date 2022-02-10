import cmath

a = int(input("Enter the value of a: \n"))      # Reading user input for value of 'a'
b = int(input("Enter the value of b: \n"))      # Reading user input for value of 'b'
c = int(input("Enter the value of c: \n"))      # Reading user input for value of 'c'

delta = ((b*b) - (4*(a*c)))     # Finding tha value of delta

eqn1 = (-b-cmath.sqrt(delta))/(2*a)     # Finding tha value for given
eqn2 = (-b+cmath.sqrt(delta))/(2*a)     # Finding tha value for given

print("The solution of Root_1 of X: ",eqn1)
print("The solution of Root_2 of Y: ",eqn2)

print("----End of Program-----")