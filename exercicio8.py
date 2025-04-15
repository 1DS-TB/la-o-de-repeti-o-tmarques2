# Calcule a soma da série harmônica até N termos: S = 1 + 1/2 + 1/3 + ... + 1/N. Arredonde o resultado para 2 casas decimais.
N = int(input("Digite um número inteiro:"))
soma = 0
serie = []

for i in range(1, N + 1):
    termo = f"1/{i}"  # Representação do termo
    serie.append(termo)
    soma += 1 / i

print("Série harmônica:", " + ".join(serie))
print(f"Soma da série harmônica até {N} termos: {soma:.2f}")