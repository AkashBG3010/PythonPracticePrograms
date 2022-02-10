import math

wind_speed = float(input("Enter the wind speed in miles/hour: \n"))
air_temp = float(input("Enter the air temperature in fahrenheit: \n"))
v = wind_speed
t = air_temp

wind_chill = (35.74 + (0.6215*t) + ((0.4275*t - 35.75)*(math.pow(v, 0.16))))
w=wind_chill
print("The wind chill index is: ", int(round(w, 0)))

print("----End of Program-----")