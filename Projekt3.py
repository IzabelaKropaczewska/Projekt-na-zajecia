

'''import random
print("Program będzie podawał liczby, twoim zadaniem będzie odpowiedzieć liczbą z zakresu od 1 do 100")
wynik_gracza = 0
wynik_komputera = 0
for i in range(10):
    wylosowana = random.randint(1,100)
    liczba = int(input())
    print("Komputer wylosował:", wylosowana)
    if wylosowana > liczba:
        wynik_komputera += 1
    elif wylosowana < liczba:
        wynik_gracza += 1
print("Wygrywała większa liczba. Twój wynik to:", wynik_gracza, ", a wynik komputera to:", wynik_komputera)
if wynik_gracza > wynik_komputera:
    print("Wygrał gracz.")
elif wynik_gracza < wynik_komputera:
    print("Wygrał komputer.")
elif wynik_gracza == wynik_komputera:
    print("Mamy remis.")'''

'''import random
liczby = 0
while liczby < 3:
    wylosowana = random.randint(100,999)
    if wylosowana %4 == 0:
        print(wylosowana)
        liczby += 1'''



'''import random
print("Czarodziej ma kapelusz. Co wyciągnie z kapelusza?")
for i in range(100):
    prawdopodobieństwo = random.random()
    print(prawdopodobieństwo)
    if prawdopodobieństwo <= 0.001:
        print("Sztabka złota!")
    elif prawdopodobieństwo <= 0.02:
        print("Konsola!")
    elif prawdopodobieństwo <= 0.1:
        print("Husteczka!")
    elif prawdopodobieństwo <= 0.5:
        print("Mikser!")
    elif prawdopodobieństwo <= 0.99:
        print("Balonik!")
    else:
        print("Nic.")'''



import os
import random
while True:
    print("Aby wyświetlić informacje o autorze wciśnij \"a\"")
    print("Aby wyświetlić program wyświetlający 3 liczby podzielne przez 4 z zakresu od 100 do 999, wciśnij \"b\"")
    print("Aby Czarodziej wyjął coś z kapelusza, wciśnij \"c\"")
    print("Aby zagrać w grę, wciśnij \"d\"")
    print("Aby zakończyć program wciśnij \"e\"")
    znak = input()
    if znak == "a":
        print("Ewa, grupa 1")
    elif znak == "b":
        liczby = 0
        while liczby < 3:
            wylosowana = random.randint(100,999)
            if wylosowana %4 == 0:
                print(wylosowana)
                liczby += 1
    elif znak == "c":
        print("Czarodziej ma kapelusz. Co wyciągnie z kapelusza?")
        prawdopodobieństwo = random.random()
        if prawdopodobieństwo <= 0.001:
            print("Sztabka złota!")
        elif prawdopodobieństwo <= 0.02:
            print("Konsola!")
        elif prawdopodobieństwo <= 0.1:
            print("Husteczka!")
        elif prawdopodobieństwo <= 0.5:
            print("Mikser!")
        elif prawdopodobieństwo <= 0.99:
            print("Balonik!")
        else:
            print("Nic.")
    elif znak == "d":
        print("Program będzie podawał liczby, twoim zadaniem będzie odpowiedzieć liczbą z zakresu od 1 do 100")
        wynik_gracza = 0
        wynik_komputera = 0
        for i in range(10):
            wylosowana = random.randint(1,100)
            liczba = int(input())
            print("Komputer wylosował:", wylosowana)
            if wylosowana > liczba:
                wynik_komputera += 1
            elif wylosowana < liczba:
                wynik_gracza += 1
        print("Wygrywała większa liczba. Twój wynik to:", wynik_gracza, ", a wynik komputera to:", wynik_komputera)
        if wynik_gracza > wynik_komputera:
            print("Wygrał gracz.")
        elif wynik_gracza < wynik_komputera:
            print("Wygrał komputer.")
        elif wynik_gracza == wynik_komputera:
            print("Mamy remis.")
    elif znak == "e":
        break
    else:
        print("Nieprawidłowy znak")
    input()
    os.system("cls")
    
    lista1 = [1,2,3,4,5,6]
def usun_nieparzyste(lista):
    dlugosc = len(lista)
    for liczba in lista[:]:
        if liczba%2 == 1:
            lista.remove(liczba)
    return lista

print(usun_nieparzyste(lista1))

lista2 = [7,8,9,10,11,12,13,14,15,16]
print(usun_nieparzyste(lista2))

lista3 = [1,1,1]
print(usun_nieparzyste(lista3))

