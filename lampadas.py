def começar():
    vida = 0
    ligada = False
    print("lampada desligada")
    
    while True:
        print("-"*10)
        p = str(input("digite algo: "))

        if p == "ligar lampada" or p == "ligar" or p == "l":
            if ligada == False:
                print("lampada ligada")
                print("-"*10)
                vida += 1
                ligada = True
    
        if p == "desligar lampada" or p == "desligar" or p == "d":
            if ligada == True:
                print("lampada desligada")
                print("-"*10)
                vida += 1
                ligada = False
            
        if p == "trocar lampada" or vida == 3:
            print("lampada queimada")
            print("-"*10)
            print("trocando lampada")
            print("-"*10)
            print("lampada trocada")
            print("-"*10)
            começar()