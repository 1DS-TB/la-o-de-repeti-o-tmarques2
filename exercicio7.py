# Peça ao o usuário um numero N. E o utilize laços aninhados para imprimir o seguinte padrão : N = 5
n = int(input("Digite um número inteiro:"))
m = " "

for i in range(1, n + 1):
    m = m + "*"
    print(m)