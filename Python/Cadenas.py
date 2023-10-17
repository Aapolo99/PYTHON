'''
print("""We only see about 60% of the Moon's surface, this is known as the "near side".""")

#Texto Multilinea
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline = """Facts about the Moon: There is no atmosphere. There is no sound."""
print(multiline)

# .title() devuelve la cadena, la primera letra de la cadena en Mayuscula.
print("temperatures and facts about the moon".title())

heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

#División de una cadena
# .split() separa la cadena en cada espacio con una ,

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures .split()
print(temperatures_list)

#Búsqueda de una cadena
temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures .split('\n')
print(temperatures_list)

#La manera más sencilla de detectar si existe una palabra, un carácter o un grupo de caracteres determinados en una cadena es usar el operador in
print("Moon" in "This text will describe facts and challenges with space travel")

print("Moon" in "This text will describe facts about the Moon")

#Un enfoque para buscar la posición de una palabra específica en una cadena consiste en usar el método .find():
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

#El método .find() devuelve -1 cuando no se encuentra la palabra, o bien devuelve el índice (el número que representa la posición en la cadena). Así es como se comportaría si busca la palabra Mars:
#Salida: 64, 64 es la posición donde "Mars" aparece en la cadena.
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))

#.count(), que devuelve el número total de repeticiones de una palabra determinada en una cadena.
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))

#.lower() devuelve la cadena, la cadena en Minuscula.
print("The Moon And The Earth".lower())
#.upper() devuelve la cadena, la cadena en Mayuscula.
print("The Moon And The Earth".upper())

#Comprobación del contenido
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])
#El código anterior confía en que todo lo que hay después de los dos puntos (:) es una temperatura. La cadena se divide en :, lo que genera una lista de dos elementos. El uso de [-1] en la lista devuelve el último elemento que, en este ejemplo, es la temperatura.

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

 #En el caso de los números negativos, el guion se agrega como prefijo al número y se puede detectar con el método .startswith():
print("-60".startswith('-'))

# .endswith() ayuda a comprobar el último carácter de una cadena:
if "30 C".endswith("C"):
    print("This temperature is in Celsius")
'''
#Transformar texto
#.replace() para buscar y reemplazar repeticiones de un carácter o grupo de caracteres.
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())

#.join() puede volver a agrupar los caracteres nuevamente.
#El método .join() necesita un elemento iterable (como una lista de Python) como argumento, por lo que su uso es diferente al de otros métodos de cadena:
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
#En este ejemplo, se usa ' ' para unir todos los elementos de la lista.