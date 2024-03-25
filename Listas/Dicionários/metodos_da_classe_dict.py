#clear:

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com":{"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com":{"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com":{"nome": "Melaine", "telefone": "3333-7766"},
}
print(contatos)
contatos.clear()
print(contatos)

#=========================================================================
#copy:

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])
print(copia["guilherme@gmail.com"])

#=========================================================================
#fromkeys:

dict.fromkeys(["nome", "telefone"])

dict.fromkeys(["nome", "telefone"], "vazio")

#=========================================================================
#get:

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

#contatos["chave"]

print(contatos.get("chave"))
print(contatos.get("chave",{}))
print(contatos.get("guilherme@gmail.com",{}))

#=========================================================================
#items:

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

print(contatos.items())

#=========================================================================
#keys:

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

print(contatos.keys())

#=========================================================================
#pop:

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

resultado = contatos.pop("guilherme@gmail.com")
print(resultado)
resultado = contatos.pop("guilherme@gmail.com",{})
print(resultado)

#=========================================================================
#popitem:

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.popitem()

#=========================================================================
#setdefault:

contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}

#ontato.setdefault("nome", "Giovanna")
#print(contato)

contato.setdefault("idade", 28)
print(contato)

#=========================================================================
#update:

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna","telefone": "3322-8181"}})
print(contatos)

#=========================================================================
#values:

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com":{"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com":{"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com":{"nome": "Melaine", "telefone": "3333-7766"},
}

print(contatos.values())

#=========================================================================
#in:

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com":{"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com":{"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com":{"nome": "Melaine", "telefone": "3333-7766"},
}

print("guilherme@gmail.com" in contatos)
print("megui@gmail.com" in contatos)
print("idade" in contatos["guilherme@gmail.com"])
print("telefone" in contatos["giovanna@gmail.com"])

#=========================================================================
#del:

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com":{"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com":{"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com":{"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

print(contatos)