def par_impar(num):
  par=0
  impar=0
  for i in range(num):
    print(i)
    if i%2==0:
      par+=1
    else:
      impar+=1 
  print("Numeros pares: ",par)
  print("Numeros impares: ",impar)

def factorial(num):
  fac=1
  for i in range(num+1):
    if(i!=0):
      fac=fac*i
  return fac   

def suma_cubos(num):
    suma=0
    for i in range(num+1):
      if(i!=0):
        suma+=pow(i,3)
    return suma

def dias_semana(num):
  if num==1:
    dia="Lunes"
  elif  num==2:
    dia="Martes"
  elif  num==3:
    dia="Miercoles"
  elif  num==4:
    dia="Jueves"
  elif  num==5:
    dia="Viernes"
  elif  num==6:
    dia="Sabado"
  elif num==7:
      dia="Domingo"
  else:
      dia="No existe"
  return dia

def listarDatos(lista):
  print("Los elementos de toda la lista son: ")
  for value in lista:
    print(value)

#Otro Metodo de horas de un colaborador
def calcular_Sueldo(precio,horas):
    sueldo=precio*horas
    if sueldo<1200:
      sueldo+=(sueldo*0.05)
    return sueldo