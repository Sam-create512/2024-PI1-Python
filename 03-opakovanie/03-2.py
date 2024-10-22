a = float(input("Zadajte veľkosť strany kocky:"))
stenova = (2 * a * a) ** 0.5
telesova = (stenova * stenova + a * a) ** 0.5
print("Stenová uhlopriečka je:" , round(stenova , 2))
print("Telesová uhlopriečka je:" , round(telesova , 2))