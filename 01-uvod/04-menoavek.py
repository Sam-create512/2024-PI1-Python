meno = input("Zadaj meno: ")
priezvisko = input("Zadaj priezvisko: ")
rok = int(input("Zadaj rok narodenia: "))
if rok >= 2025:
    print("Ešte ste sa nemohli narodiť. Váš vek by bol:" , 2025 - rok , "rokov")
    exit()
vek = 2024 - rok
if vek >= 18:
    print("Meno a priezvisko: ", meno , priezvisko)
    print("Vek: ", vek)