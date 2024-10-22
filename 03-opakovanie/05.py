rok_teraz = int(input("Zadajte aktuálny rok: "))
mesiac_teraz = int(input("Zadajte aktuálny mesiac: "))
den_teraz = int(input("Zadajte aktuálny den v mesiaci: "))
rok_od = rok_teraz - 2009 
dni_od = (rok_od * 365) + (mesiac_teraz * 30) + den_teraz
hod_od = dni_od * 24
sekund_od = hod_od * 3600
print(f"Od zavedenia eura na Slovensku prešlo {dni_od} dní")
print(f"Od zavedenia eura na Slovensku prešlo {hod_od} hodín")
print(f"Od zavedenia eura na Slovensku prešlo {sekund_od} sekúnd")