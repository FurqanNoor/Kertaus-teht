import random

with open('sanat.txt', encoding='utf-8') as f:
    data = f.read().splitlines()
print(data)

string = random.choices(data, k=2)
separator = ","
value = True
def lowercase_list(item):
            return item.lower()
while value:
    try:
        integer = int(input('Anna kokonaisluku:'))
        value = False
    except ValueError:
        print("Kokonaisluvussa ei ole desimaalia")
        continue
    else:
        for x in range(integer):
            if integer > 0:
                print(separator.join(string))


    if((integer%3==0) and (integer%5==0)):
        print (string[0],string[1])
    elif  integer % 3 == 0:
        print(string[0])
    elif integer % 5 == 0:
        print(string[1])


    round = int(input("Kuinka monta kierrosta haluat?"))
    for i in range(round):
        print(i+1)

    if random.randint(1,100) <= 25:
        print(list(map(lowercase_list,string)))

    value = True
