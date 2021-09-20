"""
print("escribe un numero")
num=int(input())
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
"""


"""
print("escribe un numero")
num=int(input())

fac=1
for i in range(num+1):
  if(i!=0):
    fac=fac*i

print("FACTORIAL ES ",fac)
"""

"""
print("escribe un numero")
num=int(input())

suma=0
for i in range(num+1):
  if(i!=0):
    suma+=pow(i,3)

print("Suma ES ",suma)
"""
for i in range(6):
  print(i)