"""
The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin

Write a sorting_hat.py program that asks the user some questions using int() and places them into one of the Houses based on their answers:

Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk

If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
Else, output the message "Wrong input."

Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

If the answer is 1, Hufflepuff +2.
Else if answer is 2, Slytherin +2.
Else if answer is 3, Ravenclaw +2.
Else if answer is 4, Gryffindor +2.
Else, output the message "Wrong input."

Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
    
If the answer is 1, Slytherin +4.
Else if the answer is 2, Hufflepuff +4.
Else if the answer is 3, Ravenclaw +4.
Else if the answer is 4, Gryffindor +4.
Else, output "Wrong input."
Lastly, print out the house with the most points!
"""
# Write code below 💖
Gryffindor = "Is Gryffindor"
Ravenclaw = "Is Ravenclaw"
Hufflepuff = "Is Hufflepuff"
Slytherin = "Is Slytherin"
Count_Gryffindor = 0
Count_Ravenclaw = 0
Count_Hufflepuff = 0
Count_Slytherin = 0

Q1 = print("Q1) Do you like Dawn or Dusk? \n\t 1) Dawn \n\t 2) Dusk \n ")
Answer1 = input()
for i in Answer1:
    if i == "1":
        Count_Gryffindor += 1
        Count_Ravenclaw += 1
    elif i == "2":
        Count_Hufflepuff += 1
        Count_Slytherin += 1
    else:
        print("Wrong input.")
        
Q2 = print("Q2) When I’m dead, I want people to remember me as: \n\t 1) The Good \n\t 2) The Great \n\t 3) The Wise \n\t 4) The Bold \n")
Answer2 = input()
for i in Answer2:
    if i == "1":
        Count_Hufflepuff += 2
    elif i == "2":
        Count_Slytherin += 2
    elif i == "3":
        Count_Ravenclaw += 2
    elif i == "4":
        Count_Gryffindor += 2
    else:
        print("Wrong input.")

Q3 = print("Q3) Which kind of instrument most pleases your ear? \n\t 1) The violin \n\t 2) The trumpet \n\t 3) The piano \n\t 4) The drum \n")
Answer3 = input()
for i in Answer3:
    if i == "1":
        Count_Slytherin += 4
    elif i == "2":
        Count_Hufflepuff += 4
    elif i == "3":
        Count_Ravenclaw += 4
    elif i == "4":
        Count_Gryffindor += 4
    else:
        print("Wrong input.")

Count_F = [Count_Slytherin, Count_Hufflepuff, Count_Ravenclaw, Count_Gryffindor]

def mayor(Count_F):
    max = Count_F[0]
    for x in Count_F:
        if x > max:
            max = x
    return max

if max(Count_F) == Count_F[0]:
    print("\n The house with the most points! "+ Slytherin)
elif max(Count_F) == Count_F[1]:
    print("\n The house with the most points! "+ Hufflepuff)
elif max(Count_F) == Count_F[2]:
    print("\n The house with the most points! "+ Ravenclaw)
elif max(Count_F) == Count_F[3]:
    print("\n The house with the most points! "+ Gryffindor)
else:
    print("\n Wrong input.")
