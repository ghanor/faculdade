numero_um = int(input("Digite um numero inteiro: "))
numero_dois = int(input("Digite um numero inteiro: "))
numero_tres = int(input("Digite um numero inteiro: "))

if (numero_um < numero_dois) and (numero_dois < numero_tres):
    print("crescente")
else:
    print("não está em ordem crescente")
