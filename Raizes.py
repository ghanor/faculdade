import math

a = int(input("Digite o valor de 'a': "))
b = int(input("Digite o valor de 'b': "))
c = int(input("Digite o valor de 'c': "))

delta = (b **2) - (4 * a * c)

if delta > 0: 
    primeira_raiz = (-b + math.sqrt(delta)) / (2 * a)
    segunda_raiz = (-b - math.sqrt(delta)) / (2 * a)
    if
        print("as raízes da equação são", primeira_raiz, "e", segunda_raiz)
elif delta == 0:
    unica_raiz = (-b) / (2 * a)
    print("a raiz desta equação é", unica_raiz)
else:
    print("esta equação não possui raízes reais")
 
