text = input("ведите текст: ")
banned = input("введите запрещенные слова через запятую: ").lower().split(",")

banned = [word.strip().lower() for word in banned]

words = text.split()
for word in range(len(words)):

    if words[word].lower().strip(".,?!") in banned:
        words[word] = "***"

new_text = " ".join(words)
print(new_text)