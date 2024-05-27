def main():
    print('Executando main')

    def funcao_interna():
        print("Excutando a função interna")

    def funcao_2():
        print("Executando a funcao 2")
    
    funcao_interna()
    funcao_2()

main()