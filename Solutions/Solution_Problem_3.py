x = int(input("Lado A   "))
y = int(input("Lado B   "))
def rectangle(A,B):
    perimeter = A * 2 + B * 2
    area = A * B
    print ("area" ,area)
    print ("perimeter" ,perimeter)
rectangle(x,y)