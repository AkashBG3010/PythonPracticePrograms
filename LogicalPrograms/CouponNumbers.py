import random       # importing random library to get random element


def generateCoupon(num_chars, code_chars, coupon):
    if num_chars <= 0:  # Checking for invalid input
        print("invalid Input")
    else:
        print("The obtained coupon Code is: \n")  # printing the random obtained coupon
        code: str = ''
        for i in range(0, num_chars):  # Iterating till the length specified
            slice_start = random.randint(0, len(code_chars) - 1)  # random of string
            code += code_chars[slice_start: slice_start + 1]  # adding element to the new string

    if len(coupon) == num_chars:  # to check if length won coupon and user coupon is same
        if coupon == code:
            print("Random coupon is: ", code)
            print("Your coupon is: ", coupon)
            print("Coupon Matches!! Congratulations, You Won!!")  # Printing the result of coupon guessing
        else:
            print("Coupon doesn't matches!!, you lost")


num_chars = int(input("Enter the length of the coupon number: \n"))         # Reading user input
coupon = str(input("Enter the coupon number(Note: Capital letters and numbers only): \n"))         # Reading user input
code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'     # String of numbers and characters

generateCoupon(num_chars, code_chars, coupon)


print("----End of Program-----")