num_dig = int(input("Digite o numero: "))
x = 2
i = 2

primo = True

while x < num_dig:
    teste = num_dig % i
    if teste == 0:
        primo = False
        break
    i = i + 1
    x = x + 1

if primo == True and num_dig != 1 and num_dig != 0:
    print("primo")
else:
    print ("nao primo")
