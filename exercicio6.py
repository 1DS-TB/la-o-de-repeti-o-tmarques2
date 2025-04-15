# Solicita ao usuário a quantidade de termos
n = int(input("Digite quantos número você quer da sequência de Fibonacci: "))

if n <= 0:
    print("O número não pode ser 0 ou negativo")

else:
    a, b = 1, 1
    print("Sequência de Fibonacci:")
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b