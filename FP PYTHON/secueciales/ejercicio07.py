"Desarrolle el programa que determine el area  y el perimetro"
"de un rectangulo sabiendo que el area=bx h, perimetro= 2x (b+h)"

print("")
base_r=float(input("Ingrese la base del rectangulo:"))
altura_r=float(input("Ingrese la altura del rectangulo:"))

area_r=base_r * altura_r
perimetro_r=2*(base_r+altura_r)
print("El area del rectangulo es",format(area_r,".2f"))
print("El perimetro del rectangulo es",format(perimetro_r,".2f"))

