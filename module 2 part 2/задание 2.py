def get_month_of_year(month_number):
  month = [
      "январь",
      "февраль",
      "март",
      "апрель",
      "май",
      "июнь",
      "июль",
      "август",
      "сентябрь",
      "октябрь",
      "ноябрь",
      "декабрь",
  ]
  if 1 <= month_number <= 12:
      return month[month_number - 1]
  else:
      return "Неверный номер дня"
user_input = int(input("Введите номер месяца (от 1 до 12): "))
print(get_month_of_year(user_input))