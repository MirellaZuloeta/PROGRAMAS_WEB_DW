lista1=["naranja","pera","manzana","melon","piña","maracuya"]
#print(lista1)
#print(lista1[:])
#print(lista1[2])
#print(lista1[0])
#print(lista1[-1])
#print(lista1[0:3])
#print(lista1[:3])
#print(lista1[1:3])
#print(lista1[2:])

lista1.append("mango")
print(lista1[:])
lista1.insert(2,"papaya")
print(lista1[:])

lista1.extend(["fresa","platano","arandano"])
print(lista1[:])

print(lista1.index("melon"))