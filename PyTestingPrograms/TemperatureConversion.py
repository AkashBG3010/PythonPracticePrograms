def conversion1(temperature):  # Function to calculate fahrenheit
    fahrenheit = (temperature * 1.8) + 32
    print(f"{temperature} in Celsius is equal to {fahrenheit} in Fahrenheit")
    print("````````````````````````````````````````````````````````````````````")
    end_sel = str(input("Try more conversion? \n Type Y/y for 'YES' and N/n for 'NO': \n"))

    if end_sel == 'Y' or end_sel == 'y':
        main()
    else:
        print("--------Thank You------")


def conversion2(temperature):  # Function to calculate celsius
    celsius = (temperature - 32) * 5 / 9
    print(f"{temperature} in Fahrenheit is equal to {celsius} in Celsius")
    print("````````````````````````````````````````````````````````````````````")
    end_sel = str(input("Try more conversion? \n Type Y/y for 'YES' and N/n for 'NO': \n"))

    if end_sel == 'Y' or end_sel == 'y':
        main()
    else:
        print("--------Thank You------")


def main():
    print("-------------Temperature Converter---------")
    print("Select 1/2---->")
    print("Enter '1' to convert fahrenheit to celsius: ")
    print("Enter '2' to convert celsius to fahrenheit: ")
    selection = int(input())  # Reading User input
    return selection


selector = main()

if (selector < 1) & (selector > 2):  # validating
    print("Please select the correct option!")  # Error message

elif selector == 1:  # validating
    temperature = float(input("Enter the temperature in fahrenheit: \n"))  # Reading User input
    conversion2(temperature)  # Function calling

else:  # validating
    temperature = float(input("Enter the temperature in celsius: \n"))  # Reading User input
    conversion1(temperature)  # Function calling

print("------End of program------")
