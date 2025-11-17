text = input("ведите текст: ")

total_chars = len(text)

words = text.split()
total_words = len(words)

glasnie = "аеёиоуыэюяaeiou"
soglasnie = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
glasnie_count = 0
soglasnie_count = 0
for char in text.lower():
    if char in glasnie:
        glasnie_count += 1
    elif char in soglasnie:
        soglasnie_count += 1



print(glasnie_count)
print(soglasnie_count)
print(total_words)