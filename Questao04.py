distancia = int(input("Por gentileza, informe a distancia a ser percorrida em km: "))

if distancia <= 200:
    valor = distancia * 0.50
    print("O valor a ser pago eh de: ", valor)

else:
    preco = distancia * 0.45
    print("O valor a ser pago pela viagem eh de: ", preco)