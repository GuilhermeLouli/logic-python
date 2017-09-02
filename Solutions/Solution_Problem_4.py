x = int(input("Qual seu peso?    "))
y = int(input("Qual seu tamanho?    "))
def data(mass, height):
    mass = mass * 10000
    phisicalCondition = mass / height ** 2 
    print(phisicalCondition)
data(x,y)