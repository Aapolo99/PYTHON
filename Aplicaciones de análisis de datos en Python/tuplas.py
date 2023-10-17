frutas = ("naranja", "fresa", "mandarina", "uva")
print(frutas)
print(len(frutas))
print((frutas[2]))
print(frutas[-1])

for fruta in frutas:
    print(fruta)

frutasLista = list(frutas)
frutasLista[0] = "pera"
#frutasLista.insert(0, "mango")
#print(frutasLista)
frutas = tuple(frutasLista)
print(frutas)

del frutas
print(frutas)