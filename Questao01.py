velocidade = int(input("Por gentileza, informe a velocidade"))
limite = 80

if velocidade > limite:
    multa= (5 * (velocidade - limite))
    print("Voce foi multado no valor de R$:", multa)

else:
    print("Tudo certo, voce esta dentro do limite de velocidade permitido")