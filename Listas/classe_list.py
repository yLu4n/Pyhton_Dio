lista = []

lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print(lista)

lista = ["Python", 1, [40,30,20]]

lista.clear()

print(lista)

lista = ["Python", 1, [40,30,20]]

lista.copy()

print(lista)

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "c#"])

print(linguagens)

linguagens = ["python", "js", "c", "java", "c#"]

print(linguagens.index("java"))
print(linguagens.index("python"))

linguagens = ["python", "js", "c", "java", "c#"]

print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))

linguagens = ["python", "js", "c", "java", "c"]

linguagens.remove("c")

print(linguagens)

linguagens = ["python", "js", "c", "java", "c"]

linguagens.reverse()

print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse = True)
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key = lambda x: len(x))
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key = lambda x: len(x), reverse = True)
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
print(len(linguagens))

linguagens = ["python", "js", "c", "java", "csharp"]
print(sorted(linguagens, key= lambda x: len(x)))

linguagens = ["python", "js", "c", "java", "csharp"]
print(sorted(linguagens, key= lambda x: len(x), reverse= True))