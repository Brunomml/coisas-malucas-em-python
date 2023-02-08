import random
n = 4

lp = ["bruno","bruna","miguel","hugo","sarah"]

lista = ["assassino","detetive","vitima","vitima","vitima"]

while True:
    escolha = random.randint(0, n)
    ep = random.randint(0, n)
    n -= 1
    
    print(f"{lp[ep]} vai ser {lista[escolha]}")
    
    lista.remove(lista[escolha])
    lp.remove(lp[ep])
    
    if n == -1:
        break
