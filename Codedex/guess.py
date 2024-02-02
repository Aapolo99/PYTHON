# Write code below 💖

guess = 0
tries = 0

while guess != 6 and tries < 3:
            if guess != 6:
                  guess = int(input("Guess the number:  "))
                  tries += 1
if tries == 3:
      print("You not got it!")
elif guess == 6:
      print("You got it!")
