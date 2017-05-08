sequencia_num = int(input("Digite um numero inteiro: "))

diferente = True
teste_igual = 1
resto = 1

while resto != 0 and diferente:  # A condição do comando while precisa ser
    # True.Se usarmos o comando OR, apenas uma precisa ser True para satisfazer
    # o while e ele continuar rodando, com o AND as duas precisam ser
    # verdadeiras caso uma seja False, ele encerra!
    teste_um = sequencia_num % 10
    resto = sequencia_num // 10
    teste_dois = resto % 10
    teste_igual = teste_um - teste_dois
    sequencia_num = resto
    if teste_igual == 0 and sequencia_num != 0:
        diferente = False

if not diferente:
    print("sim")
else:
    print("nao")
