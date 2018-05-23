zahl = int (input("gib eine Zahl ein:"))
primzahl = True

for z in range (2,zahl):
    if (zahl % z == 0):
        primzahl = False
        break

if(primzahl):
    print(zahl," ist eine Primzahl!")

else:
    print(zahl," ist keine Primzahl!")
