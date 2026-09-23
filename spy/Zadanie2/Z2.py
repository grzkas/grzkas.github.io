def multiply(value):
    value2 = ""
    for i in value:
        value2 += i * 2
    return value2


tekst = input("Wpisz tekst: ")
print("Wynik:", multiply(tekst))
