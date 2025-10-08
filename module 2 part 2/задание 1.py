def get_day_of_week(day_number):
  days = [
      "Понедельник",
      "Вторник",
      "Среда",
      "Четверг",
      "Пятница",
      "Суббота",
      "Воскресенье"
  ]
  if 1 <= day_number <= 7:
      return days[day_number - 1]
  else:
      return "Неверный номер дня"
user_input = int(input("Введите номер дня недели (от 1 до 7): "))
print(get_day_of_week(user_input))


