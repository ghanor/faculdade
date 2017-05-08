import math

p_xis = int(input("Digite a coordenada x do primeiro ponto: "))
p_yps = int(input("Digite a coordenada y do primeiro ponto: "))
r_xis = int(input("Digite a coordenada x do segundo ponto: "))
r_yps = int(input("Digite a coordenada y do segundo ponto: "))

dist_pontos = math.sqrt((p_xis - r_xis) **2 + (p_yps - r_yps) **2) 

if dist_pontos >= 10:
    print("longe")
else:
    print("perto")
