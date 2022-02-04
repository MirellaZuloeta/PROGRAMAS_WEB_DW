import miPaquete

print("OPCIONES A ELEGIR:")
print("1: Ejercicio Pares e Impares")
print("2: Ejercicio Factorial")
print("3: Ejercicio Suma de Cubos")
print("4: Hallar el dia de la semana")
print("5: Agregar Listas")
print("6: Sueldo de un trabajador")#Para usar Otro Metodo opcional

valor=int(input())
if valor==1:
  print("Ingrese Numero para contabilizar pares e Impares: ")
  numero=int(input())
  res=miPaquete.par_impar(numero)
elif valor==2:
  print("Ingrese numero para hallar el factorial: ")
  numero=int(input())
  print("El factorial de ",numero, " es: ",miPaquete.factorial(numero))

elif valor==3:
  print("Ingrese numero para hallar la suma de cubos: ")
  numero=int(input())
  print("La suma de cubos en orden ascendete de ", numero," es: ",miPaquete.suma_cubos(numero))

elif valor==4:
  print("Ingrese el numero de la semana:")
  numero=int(input())
  print("El dia de la semana es: ", miPaquete.dias_semana(numero))
elif valor==5:
  print("Ingrese cantidad de valores que desee insertar a la lista")
  numero=int(input())
  my_list=[]
  for i in range(numero):
    print("Ingrese Dato ",(i+1)," :")
    valor=input()  
    my_list.append(valor)
    miPaquete.listarDatos(my_list)
else:
  print("Ingrese el precio de cada hora en el trabajo")
  prec=float(input())
  print("Ingrese cantidad de horas laboradas:")
  hor=int(input())
  print("El sueldo final del trabajador es de : ",miPaquete.calcular_Sueldo(prec,hor)  ," soles")