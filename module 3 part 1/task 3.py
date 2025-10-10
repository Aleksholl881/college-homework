number_one = int(input("ведите начальное число диапозона: "))
number_two = int(input("ведите конечное число диапозона: "))

for number in range(number_one, number_two+1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)