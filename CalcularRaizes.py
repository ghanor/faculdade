import math

a = input(int("Digite o valor de 'a': ")
b = input(int("Digite o valor de 'b': ")
c = input(int("Digite o valor de 'c': ")

delta = (b **2) - (4 * a * c)

if delta >= 0: 
    primeira_raiz = (-b + math.sqrt(delta)) / (2 * a)
    segunda_raiz = (-b - math.sqrt(delta)) / (2 * a)
    print("As raízes da funcao sao:", primeira_raiz, "e", segunda_raiz)
if else delta == 0:
    unica_raiz = (-b) / (2 * a)
    print("A unica raiz da função e:", unica_raiz)
else:
    print("Essa funcao nao possui raizes reais")
 
