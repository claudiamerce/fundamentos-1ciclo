import  os
os.system("cls")



varones=int(input("ingrese el total de varones:"))
mujeres=int(input("ingrese el total de mujeres:"))
PVarones=(100*varones)/(varones+mujeres)
PMujeres=(100*mujeres)/(varones+mujeres)

print("")
print(f"El porcentaje de varones es [pvarones:.2f] %")
print(f"El porcentaje de mujeres es [Pmujeres:.2f] %")