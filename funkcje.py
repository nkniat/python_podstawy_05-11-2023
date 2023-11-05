def przywitanie(name):
    print("Hej", name, ", jak się masz?")

def pole_prostokata(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        return
    return a / b

imiona = ["Natalia", "Ania", "Basia", "Kamil"]

for imie in imiona:
    przywitanie(imie)

wynik = pole_prostokata(2, 5)
print("Pole prostokata:", wynik)

wynik = dzielenie(10, 0)
if wynik:
    print("Wynik dzielenia: ", wynik)
else:
    print("Coś poszło nie tak")

