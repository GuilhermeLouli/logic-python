mass = int(input("Qual seu peso?    "))
height = int(input("Qual seu tamanho?    "))
def calcIMC(mass, height):
    mass = mass * 10000
    phisicalCondition = mass / (height ** 2) 
    print("IMC: ", phisicalCondition)
calcIMC(mass, height)