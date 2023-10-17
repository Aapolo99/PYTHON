'''
#Prueba y excepción de los bloques
try:
     open('config.txt')
except FileNotFoundError:
     print("Couldn't find the config.txt file!")

#Excepción a el Leer un archivo txt
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()

#Aunque puede agrupar excepciones, solo debe hacerlo cuando no sea necesario controlarlas 
# individualmente. Evite agrupar muchas excepciones para proporcionar un mensaje de error 
# generalizado.
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

#Si necesita acceder al error asociado a la excepción, debe actualizar la línea except para 
# incluir la palabra clave as. Esta técnica es práctica si una excepción es demasiado genérica 
# y el mensaje de error puede ser útil:

try:
    open("mars.jpg")
except FileNotFoundError as err:
     print("Got a problem trying to read the file:", err)
'''
'''En este caso, as err significa que err se convierte en una variable con el objeto de excepción 
como valor. Después, usa este valor para imprimir el mensaje de error asociado a la excepción. 
Otra razón para usar esta técnica es acceder directamente a los atributos del error. Por ejemplo, 
si detecta una excepción OSError más genérica, que es la excepción primaria de FilenotFoundError 
y PermissionError, puede diferenciarlas mediante el atributo .errno:'''
'''
try:
    open("config.txt")
except OSError as err:
     if err.errno == 2:
         print("Couldn't find the config.txt file!")
     elif err.errno == 13:
        print("Found config.txt but couldn't read it")
'''
loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""

parsed_config = {}
for line in loaded_config.split('\n'):
    try:
        key, value = line.split('=')
        parsed_config[key] = value
    except ValueError:
        print(f"Unable to parse")
print(parsed_config)