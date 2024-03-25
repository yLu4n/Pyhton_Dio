#Criando sets:

print(set([1, 2, 3, 1, 3, 4]))

print(set("abacaxi"))

print(set(("palio", "gol", "celta", "palio")))

print({"python", "java", "python"})

#==============================================
#Acessando dados de um set:

numeros = {1, 2, 3, 2, 3, 3, 2, 2, 4, 5, 6, 5, 5, 6, 7}

numeros = list(numeros)

print(numeros[0:])

#==============================================
#Iterando sets:

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

#==============================================
#Função enumerate:

for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}")

#==============================================
#Metódos da classe set:
#union:
    
conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

#==============================================
#intersection:

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))

#==============================================
#difference:

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#==============================================
#symetric_difference:

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b))

#==============================================
#issubset:

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

#==============================================
#issuperset:

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

#==============================================
#isdisjoint:

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

#==============================================
#add:

sorteio = {1, 23}

print(sorteio.add(25))
print(sorteio.add(42))
print(sorteio.add(25))

#==============================================
#clear:

sorteio = {1, 23}

print(sorteio)

sorteio.clear()

print(sorteio)

#==============================================
#copy:

sorteio = {1, 23}
print(sorteio)
sorteio.copy()
print(sorteio)

#==============================================
#discard:

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)
numeros.discard(1)
numeros.discard(45)
print(numeros)

#==============================================
#pop:

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())

#==============================================
#remove:

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)
numeros.remove(0)
print(numeros)

#==============================================
#len:

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(len(numeros))

#==============================================
#in:

print(1 in numeros)
print(10 in numeros)