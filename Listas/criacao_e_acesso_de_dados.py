frutas = ['laranja', 'maçã', 'uva']
print(frutas[0])
print(frutas[2])
print(frutas[1])

frutas = ['laranja', 'maçã', 'uva', 'pera']
print(frutas[-1])
print(frutas[-3])

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ['Ferrari', 'F8', 42000000, 2020, 2900, 'São Paulo', True]
print(carro)

matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

lista = ["p", "y", "t", "h", "o", "n"]


print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])


carros = ["gol", "celta", "palio"]  

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")