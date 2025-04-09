#Peça ao usuário um número inteiro positivo N e calcule a soma de todos os números de 1 até N usando um laço while.
N = int(input("Digite um número inteiro positivo:"))
if N > 0:
    soma = 0
    i = 1
    while i <= N:
        soma += i
        i += 1
    print(f"a soma de todos os os números de 1 até {N} é {soma}.")
else:
    print("digite um número inteiro positivo.")