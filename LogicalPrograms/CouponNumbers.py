import random
num_chars = int(input("Enter the length of the coupon number: \n"))
coupon = str(input("Enter the coupon number(Note: Capital letters and numbers only): \n"))
code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if num_chars <= 0:
    print("invalid Input")
else:
    print("The obtained coupon Code is: \n")
    code: str = ''
    for i in range(0, num_chars):
        slice_start = random.randint(0, len(code_chars) - 1)
        code += code_chars[slice_start: slice_start + 1]

if len(coupon) == num_chars:
    if coupon == code:
        print("Random coupon is: ", code)
        print("Your coupon is: ", coupon)
        print("Coupon Matches!! Congratulations, You Won!!")
    else:
        print("Coupon doesn't matches!!, you lost")

print("----End of Program-----")