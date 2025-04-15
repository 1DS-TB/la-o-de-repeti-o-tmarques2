inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

kaprekar = []

for n in range(inicio, fim + 1):
    quadrado = str(n**2)
    tamanho = len(str(n))

    direita = quadrado[-tamanho:]
    esquerda = quadrado[:-tamanho] or '0'

    if int(direita) != 0 and int(esquerda) + int(direita) == n:
        kaprekar.append(n)

print("Números de kaprekar: ", kaprekar)