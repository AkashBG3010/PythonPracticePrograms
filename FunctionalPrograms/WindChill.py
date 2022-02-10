import math     # importing tha math library for mathematical operations


def calculateWindChill(v, t):       # Function to calculate the value of Wind Chill
    # Calculating the value of wind chill with specified equation
    wind_chill = (35.74 + (0.6215*t) + ((0.4275*t - 35.75)*(math.pow(v, 0.16))))
    w = wind_chill

    printWindChill(w)   # Function calling to print the value of wind chill

def printWindChill(w):
    print("The wind chill index is: ", int(round(w, 0)))    # Printing the value of wind chill


wind_speed = float(input("Enter the wind speed in miles/hour: \n"))     # Reading user input for wind speed
air_temp = float(input("Enter the air temperature in fahrenheit: \n"))      # Reading user input for air temperature
v = wind_speed
t = air_temp

calculateWindChill(v, t)        # Function Calling


print("----End of Program-----")