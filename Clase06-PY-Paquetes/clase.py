"""""
print("Ingrese su nombre: ")

nombre=input()

print("Bienvenido ", nombre)

print("Ingrese su edad: ")

edad=int(input)

if edad>=18:
    print("ERES MAYOR¡¡¡¡¡¡¡¡¡¡¡")
else:
     print("eres menor")   



for i in range(5):
    print(i)     

for i in range(2,5):
    print(i)     


for i in range(1,21,3):
    print(i)     
        """
class Persona:
    def  _init_(self,):
        self.nombre=""
        self.edad=""
    def  _init_(self,  nom, e):
        self.nombre=nom 
        self.edad=e
    def setNombre(self,nom):
        self.nombre=nom
    def setEdad(self,e):
        self.edad=e
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad


print("Ingrese su nombre: ")
nombres=input()
print("Ingrese su edad: ")
edad=int(input)

objPersona=Persona()
objPersona.setNombre(nombres)
objPersona.setEdad(edad)

print("Nombre: ",objPersona.nombre)
print("Edad:",objPersona.edad)
"""
objPersona = Persona("Kelly",28)       
print(objPersona.nombre)
"""