def check_divisbility(dividend, divisor):
    if dividend % divisor == 0:
        return str(dividend) + " is divisible by " + str(divisor)
    else:
        return str(dividend) + " is not divisible by " + str(divisor)


dividend = int(input("Enter Dividend: "))
while True:
    divisor = int(input("Enter Divisor: "))
    if divisor == 0:
        print("Pick a number other than 0")
    else:
        break
print(check_divisbility(dividend, divisor))
