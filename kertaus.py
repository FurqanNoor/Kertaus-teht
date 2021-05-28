import random

# Tässä se lukee sanat.txt tiedoston

with open('sanat.txt', encoding='utf-8') as f:
    data = f.read().splitlines()
print(data)

# Tässä on kaikki merkkijonot

string = random.choices(data, k=2)
separator = ","
value = True
while value:
    try:
        integer = int(input('Anna kokonaisluku:'))
        value = False
    except:
        print("Kokonaisluvussa ei ole desimaalia")
    else:
        for x in range(integer):
            print(separator.join(string))

# Tässä se tulostaa ensimmäisen luvun jos se on jaollinen kolmella

    num1 = integer
    if  num1 % 3 == 0:
        print(string[0])

# Tässä se tulostaa viimeisen luvun jos se on jaollinen viidellä

    elif num1 % 5 == 0:
        print(string[-1])

# Tässä se tulostaa viimeinen ja ensimmäinen sana jos luku on jaollinen kolemella ja viidellä

    elif num1%3==0 & num1%5==0:
        print (string[0 & -1])

# Tässä se tulostaa kierroksen alkaen luvusta 1 ja päättyen lukuun jonka käyttäjä on antanut.

    round = int(input("Kuinka monta kierrosta haluat?"))
    for i in range(round):
        print(i+1)

#Tässä se tulostaa satunnaisesti 25% tulostuskierooista koko sana pienillä kirjaimilla.

    if random.randint(0,100) < 24:
        print(string)

    value = True
