# Area circulo, cuadrado, triangulo

print("Calcular Areas")
print("1. Triangulo")
print("2. Circulo")
print("3. Cuadrado")

def area_triangulo():
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    base_altura = base*altura
    area_triangulo = base_altura/2
    print("El area del triangulo es: ", area_triangulo)

def area_cuadrado ():
    lado = float (input("Ingrese el lado: "))
    base_altura = lado * lado
    print ("El area del cuadrado es: ", area_cuadrado)

num = int(input("Digite un numero: "))
if num == 1:
   area_triangulo()

elif num == 2:

elif num == 3:
    area_cuadrado()
else:


