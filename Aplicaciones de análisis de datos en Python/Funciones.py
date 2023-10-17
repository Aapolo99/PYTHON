'''def mensaje():
    print("Hola desde la funcion")
    
mensaje()

def mensaje2():
    return("Hola desde la funcion 2")
    
print(mensaje2())

def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

n1 = int(input("Digite el primer numero a sumar: "))
n2 = int(input("Digite el segundo numero a sumar: "))

print(f"El resultado de la suma es: {sumar(n1, n2)}")


def maximo_de_dos(num1, num2):
    if num1 > num2:
        return num1
    return num2

def maximo_de_tres(num1, num2, num3):
    return maximo_de_dos(num1, maximo_de_dos(num2,num3))

n1= int(input("Digite el primer numero: "))
n2= int(input("Digite el segundo numero: "))
n3= int(input("Digite el tercer numero: "))

print(f"El numero maximo entre {n1}, {n2}, {n3} es: {maximo_de_tres(n1,n2,n3)}")
'''

def cadena(mensaje):
    may = 0
    min = 0
    
    for i in mensaje:
        if i.isupper():
            may += 1
        elif i.islower():
            min += 1
        else:
            pass
        
    print(f"El mensaje es {mensaje}")
    print(f"El numero de mayusculas es: {may}")
    print(f"El numero de minisculas es: {min}")
    
palabra = input("Digite el mensaje: ")
    
cadena(palabra)