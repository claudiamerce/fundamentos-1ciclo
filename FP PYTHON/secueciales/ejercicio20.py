


import os
os.system("cls")


dinero=int(input("Ingrese la cantidad de dinero : S/. "))


billetes200=dinero//200
billetes100=(dinero%200)//100
billetes50=(dinero%200)%100//50
billetes20=(((dinero%200)%100)%50)//20
billetes10=((((dinero%200)%100)%50)%20)//10
monedas5=((((dinero%200)%100)%50)%20)%10//5
monedas2=((((((dinero%200)%100)%50)%20)%10)%5)//2
monedas1=(((((((dinero%200)%100)%50)%20)%10)%5)%2)//1


print("billetes de 200 soles : ",billetes200)
print("billetes de 100 soles : ",billetes100)
print("billetes de 50 soles : ",billetes50)
print("billetes de 20 soles : ",billetes20)
print("billetes de 10 soles : ",billetes10)
print("monedas de 5 soles : ",monedas5)
print("monedas de 2 soles : ",monedas2)
print("monedas de 1 soles : ",monedas1)