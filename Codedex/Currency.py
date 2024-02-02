# Write code below 💖

co = float(input("What do you have left in pesos? "))
pe = float(input("What do you have left in soles? "))
br = float(input("What do you have left in reais? "))
usd = float(0.20)
# float(input("USD Price "))

Total = (co + pe + br) * usd

print(Total)