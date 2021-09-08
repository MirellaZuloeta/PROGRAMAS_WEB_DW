def saludo():
    print("Buenas Noches")
    print("Bienvenidos a progra WEB")

def suma():
    num1=2
    num2=6
    suma=num1+num2
    print("la suma es:",num1+num2)

def suma_v2(num1,num2):
    print("la suma es:",num1+num2)

def suma_v3(num1,num2):
    resultado=num1+num2
    return resultado

s=suma_v3(43,63)    
print("la suma es: ",s)