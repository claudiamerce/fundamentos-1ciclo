import os

os.system ("cls")




metros =int(input("digite una cantidad en metros:"))

centrimetros=metros *100
pulgadas=centrimetros/2.54
pies=pulgadas/12
yardas=pies/3

print("centrimetros:",centrimetros,".2f),"cm")
print("Pulgadas:",format(pulgadas,".2f"),"in")      
print("Pies:",format(Pies,".2f"),"ft")   
print("Yardas:",format(Yardas,".2f"),"yd")