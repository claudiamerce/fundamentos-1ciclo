
import os
os.system("cls")

"Dado dos numers enteros de 3 cifras, desarrolle el programa que muestres la cifra"
"primera y tercera cifras intercambiadas entre ambos numeros. Ejemplo 123 y 456  624 y 351"


print("")
num1=int(input("Ingrese el primer numero:"))
num2=int(input("Ingrese el segundo numero:"))

num1_C1=num1//100
num1_c2=(num1%100)//10
num1_c3=num1%10

num2_C1=num1//100
num2_c2=(num1%100)//10
num2_c3=num1%10

print("---Numeros Intercabiados---")
print("Primer Numero:",(num2_c3*100)+(num1_c2*10)+(num2_c1))
print("Segundo Numero:",(num1_c3*100)+(num2_c2*10)+(num1_c1))