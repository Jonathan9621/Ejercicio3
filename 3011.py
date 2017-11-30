# Area circulo, cuadrado, triangulo

print("Calcular Areas")
print("1. Triangulo")
print("2. Circulo")
print("3. Cuadrado")

def areaCirculo():
    radio = float(input("Ingrese el radio del circulo"))
    area = 3.1416*radio
    return area
    
def area_triangulo():
     base = float(input("Ingrese la base: "))
     altura = float(input("Ingrese la altura: "))
     base_altura = base*altura
     area_triangulo = base_altura/2
     print("El area del triangulo es: ", area_triangulo)

num = int(input("Digite un numero: "))

if num == 1:
   area_triangulo()

elif num == 2:
    area = areaCirculo()

elif num == 3:

else:
    print("El numero ingresado esta incorrecto. ")


