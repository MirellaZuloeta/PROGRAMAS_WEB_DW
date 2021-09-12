#EJEMPLOS DE LISTAS
a = ["a", "b", "c", ["d1", "d2", "d3"], "e", "f"]

# si usamos a[0] obtenemos el primer elemento de la lista
# si usamos a[3] vamos a obtener la lista de las "d"
print(a[3])

>>> ["d1", "d2", "d3"]

# pero nosotros solo queremos el segundo elemento de esta lista

print(a[3][1])

>>> "d2"

frutas = ["pera", "manzana", "kiwi", "sandia", "naranja"]
for elemento in frutas:
  print(elemento)



#EJEMPLOS DE TUPLAS
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)

tupla = 1, 2, ('a', 'b'), 3
print(tupla)       #(1, 2, ('a', 'b'), 3)
print(tupla[2][0]) #a



#EJEMPLOS DE DICCIONARIOS
diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }

print diccionario['nombre'] #Carlos
print diccionario['edad']#22
print diccionario['cursos'] #['Python','Django','JavaScript']

dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
dic1 = dic.copy()

dic1 → {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}


#EJEMPLOS DE SETS
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
 print set_mutable1
set([1, 2, 3, 4, 5, 7, 11])
 set_mutable1.add(22)
print set_mutable1
set([1, 2, 3, 4, 5, 7, 11, 22])


set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print set_mutable1
set([1, 2, 3, 4, 5, 7, 11])
 print set_mutable2
set([2, 4, 5, 8, 9, 11])
print set_mutable1.difference(set_mutable2)
set([1, 3, 7])
 print set_mutable2.difference(set_mutable1)
set([8, 9])