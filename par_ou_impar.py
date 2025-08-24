from random import randint
v = 0
print('PAR OU ÍMPAR')
while True:
    comp = randint(1,10)
    jog = int(input('Digite um numero: '))
    play = ' '
    soma = (jog + comp) % 2
    while play not in 'PI':
        play = input('Par ou Impar? [P/I] ').upper()
    print(f'Voce jogou {jog} e o computador {comp}. Total {jog + comp}.',end=' ')
    print('DEU PAR' if soma == 0 else 'DEU IMPAR')
    if play == 'P':
        if soma == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif play == 'I':
        if soma == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
if v == 1:
    print(f'Game Over! Você venceu {v} vez.')
else:
    print(f'Game Over! Você venceu {v} vezes.')
