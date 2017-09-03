password = input("Senha: ")

for i in range(0, 9):
    for j in range(0, 9):
        for k in range(0, 9):
            holder = str(i) + str(j) + str(k)

            if holder == password:
                print("A senha é: ", holder)