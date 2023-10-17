'''
#Funciones sin argumentos

def rocket_parts():
    return "payload, propellant, structure"
output = rocket_parts()
output

#Exigencia de un argumento
def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

distance_from_earth("Moon")

#Varios argumentos
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

total_days = days_to_complete(238855, 75)
round(total_days)
'''
def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank}
    """
    print(output)
    
generate_report(80,70,75)