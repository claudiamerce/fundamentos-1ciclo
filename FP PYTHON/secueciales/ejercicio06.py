import os
import math
os.system("cls")



print("")

radio=float(input("ingrese el radio del cilindro:"))
altura=float(input("ingrese el altura del cilindro:"))


areatotal=2*3.1416*radio*(radio+altura)
volumen=3.1416*radio*2*(altura)

print("el area total del cilindro es",format(areatotal,".2f"))
print("el volumne del cilindro es",format(volumen,".2f"))