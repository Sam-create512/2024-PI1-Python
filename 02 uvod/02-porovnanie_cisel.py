a = int(input("Zadaj číslo a: "))
b = int(input("Zadaj číslo b: "))
if a==b:
    print("Čísla sa rovnajú")
    exit()
if a > b:
    print("Väčšie číslo je:" , a)
else:
    print("Väčšie číslo je:" , b)
# if je podmienený príkaz 
# najskôr zistí splnenie podmienky, ak platí, tak sa vykonajú príkazy za dvojbodkou (odsadené od kraja)
# ak podmienka neplatí, vykonajú sa príkazy za else: (odsadené od kraja)