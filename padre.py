import os

arista=0.0

#input
arista=float(os.sys.argv[1])

#processing
altura=((6**(1/2))*arista)/3
volumen_tetraedro=((2**(1/2))*(arista**3))/12

#outpout
print("################################################")
print("#hallar la altura y volumen de un tetraedro")
print("################################################")
print("#")
print("################################################")
print("#arista                               :", arista)
print("#altura                               :", altura)
print("#volumen                              :", volumen_tetraedro)
print("###############################################")

#condicional
#si la altura es mayor que el volumen mas 15, entonces el tetraedro es de clase a
#si la altura y el volumen es de una diferencia de 15, entonces el tetraedro es de clase b
#si el volumen es mayor que la altura mas 15, entonces el tetraedro es de clase c
if (altura>volumen_tetraedro+15):
    print("tetraedro de clase a")
if (-15<=volumen_tetraedro-altura<=15):
    print("tetraedro de clase b")
if (volumen>altura+15):
    print("tetraedro de clase c")
