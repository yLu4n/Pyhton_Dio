class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, parada = True, correndo = False):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.parada = parada
        self.correndo = correndo
    
    def buzinar(self):
        print("plin plin....")
    
    def parar(self):
        parada = True
        print("parando bicicleta...")
        print("bicicleta parada!")

    def correr(self):
        parada = False
        correndo = True
        print("Vruuumm...")
    
    def __str__(self):
        return f"Bicicleta: cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano}, valor= {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
print("============== VENDA ==============",
      "\nCor: ", b1.cor,
      "\nModelo: ", b1.modelo,
      "\nAno: ", b1.ano,
      "\nValor: R$", b1.valor,
      "\n===================================")
print(b1.parada)
b1.buzinar()
b1.correr()
print("Parada = ", b1.parada, "// Correndo = ", b1.correndo)
b1.parar()
print("Parada = ", b1.parada, "// Correndo = ", b1.correndo)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)