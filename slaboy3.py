from random import randrange

lista = [0, 1, 2, 3, 4, 5]

numero = 6

resposta = 8

coisaqualquer = 7

n1 = randrange(len(lista))

while resposta != 'y':

    while numero != (n1):
        n1 = randrange(len(lista))
        numero = int(input('digite um numero de 0 a 5: '))
        print(n1)
        if numero != n1:
            print('voce perdeu o numero sorteado era {} tente novamente! :)'.format(n1))
        else:
            print('voce ganhou!')
    resposta = str(input(print"deseja jogar novamente digite y or n"))
    if reposta == (resposta)



