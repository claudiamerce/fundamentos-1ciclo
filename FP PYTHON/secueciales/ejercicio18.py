import os

os.system("cls")



cant_producto=int(input("Ingrese la cantidad adquirida :"))
precio_producto=float(input("Ingrese el precio del articulo :"))



importe_compra=precio_producto*cant_producto
descuento=importe_compra-(importe_compra*0.15)
importeapagar=descuento-(descuento*0.15)

print("El importe de la compra es S/.",format(importe_compra,".2f"))
print("El primer descuento fue de S/.",format(importe_compra*0.15,".2f"))
print("El segundo descuento fue de S/.",format(descuento*0.15,".2f"))
print("El importe a pagar es de S/.",format(importeapagar,".2f"))