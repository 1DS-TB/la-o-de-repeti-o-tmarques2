#Peça ao usuário um número e exiba sua tabuada de multiplicação de 1 a 10 usando um laço for.
numero = int(input("Digite um número: "))

print(f"A tabuada de {numero} é:")

for i in range(1, 11):
    tabuada = numero * i
    print(f"{numero} x {i} = {tabuada}")