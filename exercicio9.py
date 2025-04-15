# Um número perfeito é aquele cuja soma de seus divisores (exceto ele mesmo) é igual a ele mesmo. Ex: `6` (1 + 2 + 3 = 6).
# Encontre todos os números perfeitos entre 1 e 10000 usando laços.
for numero in range(1, 10001):
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma += i
    if soma == numero:
        print(numero)
