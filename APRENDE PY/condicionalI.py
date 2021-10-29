"""
print("Ingrese precio por hora:")
precio=int(input())
print("Ingrese cantidad de horas trabajadas")
horas=int(input())

sueldo=precio*horas
if sueldo<1200:
  sueldo+=(sueldo*0.05)

print("Sueldo final es de : ",sueldo)
"""

"""
print("Ingrese cantidad de vinos vendidos")
cantidad=int(input())
print("Ingrese el precio del vino")
precio=int(input())
salida=cantidad*precio
if salida>=1000:
  salida-=salida*0.1
print("La venta total fue de ",salida," soles")  
"""

"""
print("Ingrese categoria del estudiante:")
cat=int(input())

print("Se le añadirá acerca de APAFA")
if cat==1:
  costo=250
elif cat==2:
  costo=300
elif cat==3:
  costo=300
elif cat==4:
  costo=550
else:
  costo=600
  
costo+=25
print("El costo de matricula es de: ",costo)
  
"""

"""
print("Ingrese un numero")
num=int(input())

if num%10==7:
  print("El numero termina es 7")
else:
  print("No termina en 7")

"""
print("Ingrese un numero")
num=int(input())
if num==0:
  print("Es nulo")
elif num%2==0:
  print("es par")
else:
  print("es impar")