nombre = "Melissa"
contador = 0

for i in nombre:
    if i == "s":
        contador += 1
        #print(f"La letra es: {i}")
#Break despues de cumplir la condicion con el Break no se ejecuta mas el bucle
    
print(f"Se encontraron {contador} letras s")