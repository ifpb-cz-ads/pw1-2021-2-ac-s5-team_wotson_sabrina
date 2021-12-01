n1 = int(input("Por gentileza, informe o primeiro numero"))
n2 = int(input("Por gentileza, informe o segundo numero"))
n3 = int(input("Por gentileza, informe o terceiro numero"))

if ((n1 > n2 ) and (n1 > n3)):
    print("O maior numero e", n1)

elif ((n2 > n1) and (n2 > n3)):
    print("O maior numero e", n2)

else:
    print("O maior numero e", n3)

if ((n1 < n2 ) and (n1 < n3)):
    print("O menor numero e", n1)

elif((n2 < n1) and (n2 < n3)):
    print("O menor numero e", n2)

else:
    print("O menor numero e", n3)