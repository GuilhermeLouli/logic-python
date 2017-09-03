numbers = []
numberSet = []

for i in range(0, 5):
    numbers.append(int(input("Numero: ")))

for number in numbers:
    if number not in numberSet:
        numberSet.append(number)

print(numberSet)