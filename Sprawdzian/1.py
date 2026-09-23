ocena = int(input("Podaj swój wynik w procentach (0-100): "))

def addspace():
    
    if (ocena >= 90): wychodzi = "Ocena: Celująca!"
    elif (ocena >= 89 == ocena <=70): wychodzi = "Ocena: dobra. Dobra robota!"
    elif (ocena >= 50 or ocena <= 69): wychodzi = "Ocena: dostateczna. musisz jeszcze poćwiczyć"
    elif (ocena < 50): wychodzi = "Ocena: niedostateczna. widzimy sie na poprawce"
    print(wychodzi)

