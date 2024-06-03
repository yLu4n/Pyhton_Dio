from datetime import datetime, timedelta, date, time

tipo_de_carro = 'M' # P, M, G
tempo_p = 30
tempo_m = 45
tempo_g = 60
data_atual = datetime.now()


match tipo_de_carro:
    case 'P':
        data_estimada = data_atual - timedelta(days= tempo_p)
        print(f"O carro chegou às: {data_atual} // Ficará pronto às: {data_estimada}")
    case 'M':
        data_estimada = data_atual - timedelta(days= tempo_m)
        print(f"O carro chegou às: {data_atual} // Ficará pronto às: {data_estimada}")
    case 'G':
        data_estimada = data_atual - timedelta(days= tempo_g)
        print(f"O carro chegou às: {data_atual} // Ficará pronto às: {data_estimada}")

print(date.today() - timedelta(days= 1))

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours= 1)
print(resultado.time())

if tipo_de_carro == 'P':
    data_estimada = data_atual - timedelta(days= tempo_p)
    print(f"O carro chegou às: {data_atual} // Ficará pronto às: {data_estimada}")
elif tipo_de_carro == 'M':
    data_estimada = data_atual - timedelta(days= tempo_m)
    print(f"O carro chegou às: {data_atual} // Ficará pronto às: {data_estimada}")
else:
    data_estimada = data_atual - timedelta(days= tempo_g)
    print(f"O carro chegou às: {data_atual} // Ficará pronto às: {data_estimada}")