n = int(input("Zadajte počet opakovaní n:"))
faktorial = 1
for i in range(n):
    faktorial = faktorial * (i + 1)
print(f"{n}! = {faktorial}") # {} zátovorky napíšeme pravý alt+b , alt+n {} } 