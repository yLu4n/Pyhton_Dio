menu = """
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

-> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    op = input(menu)

    match op:
        case "1":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato == f"Depósito: R${valor:. 2f}\n"
            else:
                print("Operação falhou: valor informado inválido")
        
        case "2":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques > LIMITE_SAQUES

            
        case "3":

        case "4":
