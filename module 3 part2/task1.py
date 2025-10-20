first_number = int(input("введите первое число: "))
second_number = int(input("введите второе число: "))

sum_even = 0
sum_odd = 0
sum_multiple_9 = 0
count_even = 0
count_odd = 0
count_multiple_9 = 0

for number in range(first_number, second_number + 1):

    if number % 2 == 0:
        sum_even += number
        count_even += 1
    else:
        sum_odd += number
        count_odd += 1

    if number % 9 == 0:
        sum_multiple_9 += number
        count_multiple_9 += 1

print("=" * 40)
print("сумма чётных: ", sum_even)
print("среднеарифметическое чётных: ", sum_even / count_even)
print("=" * 40)
print("сумма нечётных : ", sum_odd)
print("среднеарифметическое нечётных: ", sum_odd / count_odd)
print("=" * 40)
print("сумма кратных 9: ", sum_multiple_9)
print("среднеарифметическое кратных 9: ", sum_multiple_9 / count_multiple_9)
print("=" * 40)