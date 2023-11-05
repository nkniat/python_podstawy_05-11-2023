liczby = [-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]

liczbyParzyste = []
for liczba in liczby:
    if liczba % 2 == 0:
        liczbyParzyste.append(liczba)
print("Lista liczby zawiera: ", liczby)
print("Lista liczbyPrzyste zawiera: ", liczbyParzyste)

doPotegiDrugiej = []
for liczba in liczby:
    doPotegiDrugiej.append(liczba ** 2)
print("Lista doPotegiDrugiej zawiera: ", doPotegiDrugiej)

kwadraty = [element ** 2 for element in liczby]
print("Lista kwadraty zawiera: ", kwadraty)

kwadraty2 = [element ** 2 for element in range(1001)]
print("Lista kwadraty2 zawiera: ", kwadraty2)

parzyste = [element
            for element in liczby
            if element % 2 == 0]
print("Lista parzyste zawiera: ", parzyste)

