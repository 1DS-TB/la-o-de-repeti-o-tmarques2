#Peça ao usuário um número e verifique se ele é primo usando um laço. Um número primo é divisível apenas por 1 e por ele mesmo.
num = int(input("Digite um número: "))

if num <= 1:
    print("O número não pode ser 0 ou negativo.")

else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} não é primo")
            break

    else:
        print(f"{num} é primo")