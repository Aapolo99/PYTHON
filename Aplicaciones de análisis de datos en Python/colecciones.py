nombres = ["Johan","Mar","Juan","Maria"]
'''print(nombres)
print(nombres[1])
print(nombres[-1])
print(nombres[0:2])
print(nombres[:3])
print(nombres[1:])
print(nombres[:])
print(nombres[2::])
print(nombres[::3])
'''
nombres[3]="Laura"
print(nombres)
print(len(nombres))
nombres.append("Alejandro")
print(nombres)
nombres.insert(0, "Marco")
print(nombres)
nombres.remove("Alejandro")
print(nombres)
nombres.pop()
print(nombres)
del nombres[0]
print(nombres)
nombres.clear()
print(nombres)
#Eliminar la lista
del nombres
print(nombres)