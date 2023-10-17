'''
def water_left(5, 100, 2):
    daily_usage = 5 * 11
    total_usage = daily_usage * 2
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {5} astronauts after {2} days!")
    return f"Total water left after {2} days is: {total_water_left} liters"

#Tipo de datos no admintidos
def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypeError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"
'''
true_values = ['yes', 'y']
false_values = ['no', 'n']

# Enter code below
def str_to_bool(value):
    value = value.lower()
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError("Invalid entry")
    
# Test function here
str_to_bool("y")