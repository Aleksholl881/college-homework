text = input("Введите текст: ")

sentences = 0
for char in text:
    if char in '.!?':
        sentences += 1
if sentences == 0 and text:
    sentences = 1

words = len(text.split())

punctuation = 0
for char in text:
    if char in '.,!?;:-""()':
        punctuation += 1

print(f"Предложений: {sentences}")
print(f"Слов: {words}")
print(f"Знаков препинания: {punctuation}")