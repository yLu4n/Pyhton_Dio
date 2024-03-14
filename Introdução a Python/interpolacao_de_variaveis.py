nome = "Luan"
idade = 18
profissao = "Estágiario"
linguagem = "Python"

print ("Olá, meu nome é %s. Tenho %d anos de idade, sou %s e estou matriculado no curso de %s." % (nome,idade,profissao,linguagem))


nome = "Luan"
idade = 18
profissao = "Estágiario"
linguagem = "Python"

dados = {"nome": "Luan", "idade": 18, "profissao": "Estágiario", "linguagem": "Python"}

print ("Olá, me chamo {}. Tenho {} anos de idade, sou {} e estou matriculado no curso de {}.".format(nome,idade,profissao,
                                                                                                     linguagem))
print ("Olá, me chamo {3}. Tenho {2} anos de idade, sou {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade,
                                                                                                         nome))
print ("Olá, me chamo {nome}. Tenho {idade} anos de idade, sou {profissao} e estou matriculado no curso de {linguagem}.".format(nome = nome, idade = idade,
                                                                                                                                profissao = profissao, linguagem = linguagem))
print ("Olá, me chamo {nome}. Tenho {idade} anos de idade, sou {profissao} e estou matriculado no curso de {linguagem}.".format(**dados))


nome = "Luan"
idade = 18
profissao = "Estágiario"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Tenho {idade} anos de idade, sou {profissao} e estou matriculado no curso de {linguagem}.")


PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")


