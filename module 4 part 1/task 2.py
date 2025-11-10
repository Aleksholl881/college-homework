text = input("Введите текст: ")


reserved_words_input = input("Введите список зарезервированных слов через пробел: ")
reserved_words = reserved_words_input.split()

result_text = text

for word in reserved_words:
    result_text = result_text.replace(word, word.upper())

print("Измененный текст:")
print(result_text)