filename = input("Введите имя файла: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()

        total_lines = len(lines)
        total_words = 0
        total_chars = 0
        empty_lines = 0

        for line in lines:
            total_chars += len(line)
            total_words += len(line.split())
            if line.strip() == '':
                empty_lines += 1

        print(f"всего строк: {total_lines}")
        print(f"всего слов: {total_words}")
        print(f"всего символов: {total_chars}")
        print(f"пустых линей: {empty_lines}")
except FileNotFoundError:
    print("Файл не найден,попробуйте снова")