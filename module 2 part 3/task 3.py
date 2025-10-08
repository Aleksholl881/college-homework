price = int(input("Введите стоимость разговора: "))
operator_sender = input("Выберите оператора отправителя: ")
operator_addressee = input("Выберите оператора получателя: ")

if operator_sender == operator_addressee:
    print(price*1)
if operator_sender == "MTS" and operator_addressee == "Tele2":
    print(price*2)
if operator_sender == "MTS" and operator_addressee == "Megafon":
    print(price*2.5)
if operator_sender == "MTS" and operator_addressee == "Beeline":
    print(price*1.5)
if operator_sender == "megafon" and operator_addressee == "Tele2":
    print(price * 2)
if operator_sender == "megafon" and operator_addressee == "MTS":
    print(price * 2.5)
if operator_sender == "megafon" and operator_addressee == "Beeline":
    print(price * 1.5)
if operator_sender == "MTS" and operator_addressee == "Tele2":
    print(price*2)
if operator_sender == "MTS" and operator_addressee == "Megafon":
    print(price*2.5)
if operator_sender == "MTS" and operator_addressee == "Beeline":
    print(price*1.5)
if operator_sender == "megafon" and operator_addressee == "Tele2":
    print(price * 2)
if operator_sender == "megafon" and operator_addressee == "MTS":
    print(price * 2.5)
if operator_sender == "megafon" and operator_addressee == "Beeline":
    print(price * 1.5)