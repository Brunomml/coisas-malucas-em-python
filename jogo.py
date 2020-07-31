def sorte():
    from random import randint
    n = 0
    r = randint(1, 10)
    while True:
        n = int(input('digite um numero: '))
        
        if n == 0:
            break
            
        if n == r:
            print('vc acertou')
            break
            
        elif n < r:
            print('chute um numero maior')
            
        else:
            print('chute um numero menor')
    print('---fim de jogo---')
		