from random import randint

number = randint(1, 10)

x = int(input("Chute    "))

if x == number:
    print("Parabens, vc acertou")
else:
    print("Que pena, o numero era: ", number)
