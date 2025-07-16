import os

os.system("cls")

"una persona ha recorrido tres tramo en pies y el tercer tramo de una carretera. La longitud del primer tramo "
"esta dada en kilometros, el segundo tramo en pies y el tercer tramo en millas."
"Desarrolle el programa que deermien la longitud total recorrida en metros y en yardas."
"considere los siguientes factores de conversion: 1 metro= 3.2808 pies. 1 milla = 1609 metros"

print("")

kilometros=float(input)("longitud del primer tramo( kilometros):")
pies=float(input)("longitud del segundo tramo(Pies):")
millas=float(input)("longitud del tercer tramo(Millas):")

primer_tramo=kilometros*1000
segundo_tramo=Pies/3.2808
tercer_tramo=Millas*1609
total_metros=primer_tramo+segundo_tramo+terce_tramo
total_yardas=(total_metros*3.2808)/3

print("total en metros:",format(total:metros,".2f),"m")
print("total en metros:",format(total:metros,".2f),"yd")
                        