names = {"Natalia", "Kleopatra", "Gustaw", "Radosław", "Marek", "Dorota"}

namesLen = {
    name: len(name)
    for name in names
    if name.startswith("N")
}

print("Słownik na bazie zbioru: ", namesLen)

# {1: 1,
#  2: 4,
#  3: 9,
#  4: 16,
#  5: 25}

liczby = {
    liczba: liczba **2
    for liczba in range(6)
}
print(liczby)

liczby = { 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 }

liczbyKwadrat = {
    liczba: liczba * liczba
    for liczba in liczby
}

print(f'Liczba razy liczba: {liczbyKwadrat}')

celcius = {'t1': 7, 't2': 10, 't3': 11, 't4': 10, 't5': 5}

fahrenheit = {
    key: value * 1.8 + 32
    for key, value in celcius.items()
    if value > 0
}

print("Fahrenheit: ", fahrenheit)