def czy_doskonala(n):
    dzielniki = 0
    for y in range(1, n):
        if n % y == 0:
            dzielniki += y

    if dzielniki == n:
        return True
    return False


while True:
    dol = int(input("Podaj początek przedziału: "))
    gor = int(input("Podaj koniec przedziału: "))

    if dol > gor or gor <= 1 or dol <= 1:
        print("Początek musi być mniejszy od końca, a obie liczby muszą być większe od 1")

    else:
        break


suma = 0
licznik = 0
for i in range(dol, gor + 1):
    if czy_doskonala(i):
        print("Liczba doskonała:", i)
        suma += i
        licznik += 1

print("Ilość liczb doskonałych =", licznik)
print("Suma liczb doskonałych =", suma)
