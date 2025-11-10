speech = input("ведите предложение палиндром:")
speech = speech.lower()
speech = speech.replace(" ", "")

speech_obratno = speech[::-1]

if speech_obratno == speech:
    print(f"это палиндром")
else:
    print("это не палиндром")


