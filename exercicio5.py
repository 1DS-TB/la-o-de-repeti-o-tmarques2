#Peça ao usuário um número e verifique se ele é primo usando um laço. Um número primo é divisível apenas por 1 e por ele mesmo.
num1 = int(input("Digite um número:"))

for i in range(2, num1):
    if num1 % i == 0:
        break

else:
    print(num1==)