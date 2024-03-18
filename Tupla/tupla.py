#Criando tuplas:

frutas = ("laranja", "pera", "uva")

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

#==========================================
#acessando dados em uma tupla:

frutas = ("maçã", "laranja", "pera", "uva",)
print(frutas[0])
print(frutas[3])
print(frutas[-1])
print(frutas[-3])

#==========================================
#criando tuplas dentro de uma tupla:

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

#==========================================
#fatiamento de uma tupla:

tupla = ("p", "y", "t", "h", "o", "n")

print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])

#==========================================
#metódos da classe tupla:

cores = ("vermelho", "azul", "verde", "azul")

print(cores.count("vermelho"))
print(cores.count("verde"))
print(cores.count("azul"))

linguagens = ("python", "js", "c", "csharp",)

print(linguagens.index("c"))
print(linguagens.index("python"))

linguagens = ("python", "js", "c", "csharp", "java",)

print(len(linguagens))