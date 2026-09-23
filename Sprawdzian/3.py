while True:
    dol = int(input("Podaj początek przedziału: "))
    gor = int(input("Podaj koniec przedziału: "))

    if (gor > dol>1) :
        break
    else:
        print("Początek musi być mniejszy od końca, a obie liczby muszą być większe od 1")
ilosc = 0
suma = 0

for x in range (dol, gor + 1):
    czy_pierwsza = True

    if x % 2:
        czy_pierwsza = False
    for i in range(2, int (x ** 0.5)):
        if (x % i == 0):
            czy_pierwsza = True
            break
    
    if czy_pierwsza == True:
        print(f"Liczba: {x}")
        ilosc += 1
        suma += x
print(f"Ilość liczb = {ilosc}" )
print(f"Suma = {suma}")