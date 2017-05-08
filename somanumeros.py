num = input("Digite o numero: ")
x = len(num)
y = 0
num_dig = int(num)
soma_final = 0
while y <= x:
    prim_soma = num_dig % 10 #1) Pega o numero da direita pra somar e armazena em prim_som Ex: 4567 ele armazena o 7 4)Pega 456 que esta no num_dig e separa o primeiro da direita Ex:456 ele armazena o 6
    resto = num_dig // 10 #2) Armazena o resto do numero em resto Ex:456 5) Armazena o do numero em resto Ex: 45
    soma_final = soma_final + prim_soma #3) soma a soma_final que no caso e 0 mais a prim_soma Ex: 0 + 7 6)Soma a soma_final que agora e 7 mais a prim_soma que agora e 6 Ex: 7 + 6
    num_dig = resto #4) num_dig agora vira a variavel resto Ex: 456 7) continua...
    y = y + 1 #Serve como incremento para o while continuar até o tamanho do numero digitado
print(soma_final)
