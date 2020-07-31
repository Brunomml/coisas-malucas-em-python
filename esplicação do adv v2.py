import random

"sistema de parar o loop"
n = 4

"listas"
lp = ["bruno","bruna","miguel","hugo","sarah"]
lista = ["assascino","detetive","vitima","vitima","vitima"]

"loop de escolha"
while True:
    
    "escolha de quem ou do que ela vai ser"
    escolha = random.randint(0, n)
    ep = random.randint(0, n)
    
    "sistema de parar o loop"
    n -= 1
    
    "mostra na tela as escolhas"
    print(f"{lp[ep]} vai ser {lista[escolha]}")
    
    "remove o que ja foi escolido"
    lista.remove(lista[escolha])
    lp.remove(lp[ep])
    
    "sistema de parar o loop"
    if n == -1:
        break