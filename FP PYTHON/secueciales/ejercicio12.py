
import os
os.system("cls")


print("")
num_segundos=int(input("Digite un numero expresado en segundo:"))

dias=((num_segundos//60)//60)//24
hora=((num_segundos//60)//60)%24
minutos=((num_segundos//60)%60)
segundo=(num_segundos60%60)
          
print("dias: ",dias)
Print("horas: ",hora)
Print("minutos: ",minutos)
Print("segundos: ",segundos)
print("")
