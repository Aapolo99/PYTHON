# Write code below 💖

num = 100
#i = 1

for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        i += 1
    elif i % 3 == 0:
        print("Fizz")
        i += 1
    elif i % 5 == 0:
        print("Buzz")
        i += 1
    else:
        print(i)
