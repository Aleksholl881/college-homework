def call_counter (func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1

        if wrapper.count % 10 == 1 and wrapper.count % 100 != 11:
            times_word = "раз"
        else:
            times_word = "раза"

        print(f"Функция {func.__name__} вызвана {wrapper.count} {times_word}")
        print(f"Аргументы: {args}{f', {kwargs}' if kwargs else ''}")

        result = func(*args, **kwargs)
        return result

    wrapper.count = 0
    return wrapper

@call_counter
def add(a, b):
    return a + b

@call_counter
def repeat(text, n):
    return text * n

if __name__ == "__main__":

    print(add(2, 3))
    print()

    print(add(10, 5))
    print()

    print(add(7, 8))
    print()

    print(repeat('Hi', 3))
    print()

    print(repeat('Hello', 2))
    print()