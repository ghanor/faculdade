decrescente = True
anterior = int(input("Digite o primeiro numero: "))
valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite o proximo numero: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente: #Porque decrescente ja tem o valor True
    print("Esta em ordem decrescente")
else:
    print("Nao esta em ordem decrescente")

