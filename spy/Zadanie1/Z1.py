def ocen_pogode(temp):
    if 0 < temp <= 14:
        print("Chłodno, Potrzebna kurtka.")
    elif temp <= 25:
        print("Jest przyjemnie. Bluza powinna wystarczyć.")
    else:
        print("Jest gorąco! Załóż t-shirt.")


temperatura = int(input("Ile jest stopni Celsjusza? "))
ocen_pogode(temperatura)
