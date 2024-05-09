import textwrap

def menu():
    menu = """\n
    ================== MENU ==================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar contas
    [7] Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /): #Recebe os argumentos de forma posicional

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n ||| Depósito realizado com sucesso! |||")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):#Recebe os argumentos de forma nomeada
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Não possui saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excedeu o limte.")
    elif excedeu_saques:
        print("Operação falhou! Limite máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("||| Saque realizado com sucesso! |||")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato

def exibir_extrato(saldo,/,*, extrato):#Recebe o argumento saldo de forma posicional e o argumento extrato de forma nomeada
    if extrato == "":
                    print("\n================== EXTRATO ==================")
                    print("Não foram realizadas movimentações." )
                    print(f"\nSaldo: R$ {saldo:.2f}")
                    print("================================================")
    else:
        print("\n================== EXTRATO ==================")
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (não inserir . ou -)")
    usuario = verificar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com este CPF! Verifique se digitou corretamente! @@@")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("||| Usuário criado com sucesso! |||")

def verificar_usuario(cpf, usuarios):
     usuarios_verificados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_verificados[0] if usuarios_verificados else None

def criar_conta(agencia, numero_conta, usuarios):
     cpf = input("Informe o CPF (não inserir . ou -)")
     usuario = verificar_usuario(cpf, usuarios)

     if usuario:
          print("\n||| Conta criada com sucesso! |||")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     print("\n@@@ Usuário não encontrado, processo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
"""
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITES_SAQUES = 3
    AGENCIA = "00001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        op = menu()
        if op <=7:
            match op:
                case "1":
                    valor = float(input("Informe o valor do depósito: "))
                    saldo, extrato = depositar(saldo, valor, extrato)
                case "2":
                    valor = float(input("Informe o valor do saque: "))

                    saldo, extrato = sacar(
                        saldo = saldo,
                        valor = valor,
                        extrato = extrato,
                        limite = limite,
                        numero_saques = numero_saques,
                        limite_saques = LIMITES_SAQUES,
                    )
                case "3":
                    exibir_extrato(saldo, extrato= extrato)
                
                case "4":
                    criar_usuario(usuarios)
                case "5":
                    numero_conta = len(contas) + 1
                    conta = criar_conta(AGENCIA, numero_conta, usuarios)

                    if conta:
                        conta.append(conta)
                case "6":
                    listar_contas(contas)
                case "7":
                    break
        else:
             print("Operação inválida, por favor digite novamente a operação que deseja realizar.")
main()