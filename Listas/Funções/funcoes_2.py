def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca= "Fiat", motor= "1.0", combustivel= "Gasolina") #válido

#criar_carro(modelo = "Palio", ano = 1999, placa = "ABC-1234", marca= "Fiat", motor= "1.0", combustivel= "Gasolina") inválido

#=============================================================================================================================

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro(modelo= "Palio", ano= 1999, placa= "ABC-1234", marca= "Fiat", motor= "1.0", combustivel= "Gasolina") #válido

#criar_carro( "Palio",  1999,  "ABC-1234", marca= "Fiat", motor= "1.0", combustivel= "Gasolina") inválido

#========================================================================================================================

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca= "Fiat", motor= "1.0", combustivel= "Gasolina") #válido

#criar_carro(modelo= "Palio", ano= 1999, placa= "ABC-1234", marca= "Fiat", motor= "1.0", combustivel= "Gasolina") #inválido

#========================================================================================================================
#Objetos de primeira classe:

def somar(a, b):
    return a+ b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)

op = somar

print(op(1,23))

salario = 2000

def salario_bonus(bonus, lista):
    global salario
    
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario += bonus
    return salario

lista = [1]
salario_bonus(500, lista)
print(salario)
print(lista)
