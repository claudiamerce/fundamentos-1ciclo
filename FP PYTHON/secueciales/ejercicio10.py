
import os
os.system("cls")

 "Dado un numero natrual de cuatro cifras, desarrole el programa que permite obterne"
 "el numero al reves Ejemplo 1234 4321"


print("")
numero=int(input("Inggrese un numero:"))

cl=numero//1000
c2=(numero%1000)//100
c3=(((numero%1000)%100)//100)
c4=numero%10

print(c1)
print(c2)
print(c3)
print(c4)