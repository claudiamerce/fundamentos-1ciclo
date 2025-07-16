

import os
os.system("cls")


montototal=float(input("Ingrese monto total vendido :"))


comision=(montototal*9)/100
sueldobruto=500+comision
descuento=(sueldobruto*11)/100
sueldoneto=sueldobruto-descuento


print("Comision : S/.",format(comision,".2f"))
print("sueldo bruto : S/.",format(sueldobruto,".2f"))
print("descuento : S/.",format(descuento,".2f"))
print("sueldo neto : S/.",format(sueldoneto,".2f"))

                                            
                              