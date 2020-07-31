def tabu():
    n = 0
    while True:
        n = int(input('digite um numero: '))
        n1 = 0
        n2 = 0
        if n == 0:
            break
        for c in range(1, 11):
            n1 += 1
            n2 += n
            print(f'{n} x {n1} = {n2}')
    print('    ---fim---')
