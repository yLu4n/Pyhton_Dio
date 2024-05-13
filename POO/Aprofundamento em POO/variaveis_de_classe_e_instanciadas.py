class Estudante:
    universidade = "UCSal"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    

    def __str__(self) -> str:
        return f"Nome: {self.nome} ({self.matricula}) - {self.universidade}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    

pessoa = Estudante("Guilherme", 169812315)
pessoa_2 = Estudante("Giovanna", 225001155)
print(pessoa)
print(pessoa_2)
mostrar_valores(pessoa, pessoa_2)

Estudante.universidade = "Python"
pessoa_3 = Estudante("Chappie", 3)
mostrar_valores(pessoa, pessoa_2, pessoa_3)
