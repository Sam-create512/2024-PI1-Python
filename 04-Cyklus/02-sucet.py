n = int(input("Zadajte počet opakovaní n:"))
sucet = 0
for i in range(n):
    sucet = sucet + (i + 1) # sucet + (i + 1) je výraz, najskôr sa vypočíta výraza výsledná hodnota sa priradí do premennej sucet
    # print(i, i+1, sucet)
print("Súčet prvých", n , "čísel je:", sucet)