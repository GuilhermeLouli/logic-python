sideA = int(input("Lado A   "))
sideB = int(input("Lado B   "))
def calcAreaAndPerimeter(sideA, sideB):
    perimeter = sideA * 2 + sideB * 2
    area = sideA * sideB
    print ("area: ", area)
    print ("perimeter: ", perimeter)
calcAreaAndPerimeter(sideA, sideB)