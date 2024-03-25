pessoa = {"nome": "Luan", "idade": 19}

pessoa = dict(nome= "Luan", idade= 19)

pessoa["telefone"] = "3333-1234"
print(pessoa)

pessoa["nome"] = "Maria"
print(pessoa)
#============================================================

dados = {"nome": "Luan", "idade": 19, "telefone": "3333-1234"}

dados["nome"]
dados["idade"]
dados["telefone"]

print(dados)

dados["nome"] = "Sabrina"
dados["idade"] = 23
dados["telefone"] = "9988-1781"

print(dados)

#==============================
#dicionarios aninhados

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "luan@gmail.com": {"nome": "Luan", "telefone": "3443-2121"},
    "cahppie@gmail.com":{"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com":{"nome": "Melaine", "telefone": "3333-7766"},
}

print(contatos["luan@gmail.com"]["telefone"])

#=======================================================================
#iterar

for chave in contatos:
    print(chave, contatos[chave])

for valor in contatos.items():
    print(chave, valor)