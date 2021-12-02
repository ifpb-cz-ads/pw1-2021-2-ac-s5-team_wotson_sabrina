salario = float(input("Por gentileza, informe seu salario"))

if salario > 1250:
    aumento = (salario * (10 / 100))
    total = salario + aumento
    print("O seu salario com aumento foi de: ", total, "e o valor do seu aumento foi de:", aumento)

else:
    aumento1 = (salario * (15 / 100))
    total1 = salario + aumento1
    print("O seu salario com aumento foi de: ", total1, "e o valor do seu aumento foi de:", aumento1)