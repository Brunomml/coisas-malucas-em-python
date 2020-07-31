def começar():
    from random import randint
    print("para ver a regra do jogo é so digitar\nregra")
    print("lampada desligada")
    ligada = False
    while True:
        pessoa = str(input("digite algo:"))
        vida = randint(1, 13)
        if pessoa == "l":
            if ligada == False:
                print("lampada ligada")

        if pessoa == "d":
            if ligada == True:
                print("lampada desligada")
    
        if vida == 0:
            print("você perdeu")
            r = str(input("você quer recomeçar?"))
            if r == "sim":
                começar()
            if r == "nao" or r == "não":
                print("fim de jogo")
                break
        if pessoa == "trocar":
            
        if pessoa == "regras" or pessoa == "regra":
            print("o jogo ")
começar()