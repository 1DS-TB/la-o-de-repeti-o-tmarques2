#Peça ao usuário um número inteiro positivo e calcule seu fatorial usando um laço for ou while. Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120.
N = int(input("Digite um número inteiro positivo:"))

if N >= 0:
    fatorial = 1
    for i in range(1, N+1):
        fatorial *= i

    print(f"{N}! = {fatorial}")
else:
    print("Número inválido")

