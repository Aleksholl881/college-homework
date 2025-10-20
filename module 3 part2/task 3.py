number = int(input())
while number != 7:

    if number > 0:
        print("number is positive")
        break
    elif number < 0:
        print("number is negative")
        break
    elif number == 0:
        print("number is equal zero")
        break
if number ==7:
    print("good bye")
