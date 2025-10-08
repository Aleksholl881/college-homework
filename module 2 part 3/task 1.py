number = int(input("введите число от 1 до 100: "))
for i in range(number):
    if i > 100 or i < 1:
        print(f"{i} неверное число")
    elif i % 3 == 0 and i % 5 == 0:
        print(f"{i} fizz buzz")
    elif i % 5 == 0:
        print(f"{i} buzz")
    elif i % 3 == 0:
        print(f"{i} fizz")
    else:
        print(i)