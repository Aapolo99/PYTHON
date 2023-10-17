planetas = {"tierra", "marte", "jupiter"}
print(planetas)
print(len(planetas))
print("marte" in planetas)
print("saturno" in planetas)
planetas.remove("tierra")
print(planetas)
planetas.discard("marte")
print(planetas)
planetas.clear()
print(planetas)
del planetas
print(planetas)