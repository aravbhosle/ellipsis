def lcm(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1
    return lcm


while True:
    x = int(input("Enter a number: "))
    if x == 0:
        print('Choose number other than 0')
    else:
        break

while True:
    y = int(input("Enter a number: "))
    if y == 0:
        print('Choose number other than 0')
    else:
        break

print(lcm(x, y))
