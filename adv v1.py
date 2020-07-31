import random
n = 4
pp = int(input("digite o numero de pessoas:"))
jj = False

if pp == 4:
    n = 3
    jj = True
    
lista = ["assascino","detetive","vitima","vitima","vitima"]

while True:
    if pp > 5:
        print("desculpa so pode 5 pessoas")
        break
        
    if pp <= 3:
        print("desculpa poucas pessoas para jogar")
        break
        
    if n == 4:
        if jj == True:
            lista.remove(lista[4])
            
    escolha = random.randint(0, n)
    n -= 1
    print(f"você vai ser {lista[escolha]}")
    lista.remove(lista[escolha])
    
    if n == -1:
        break