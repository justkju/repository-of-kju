from random import randrange

lista = [0, 1, 2, 3, 4, 5]

numero = 7

resposta = 'y'

n1 = randrange(len(lista))

while resposta == 'y' or resposta == 'Y':
    while numero != (n1):
        n1 = randrange(len(lista))
        numero = int(input('digite um numero de 0 a 5: '))
        if numero > 5 or numero < 0:
            while numero > 5 or numero < 0:
                if numero < 0:
                    print("este numero é menor que 0")
                    numero = int(input('digite um numero de 0 a 5: '))
                if numero > 5:
                    print("esse numero e maior que 5 ")
                    numero = int(input('digite um numero de 0 a 5: '))
        if numero != n1:
            print('voce perdeu o numero sorteado era {} tente novamente! : )'.format(n1))
        else:
            print('voce ganhou!')
    resposta = (input("deseja jogar novamente se sim digite y "))
    numero = 7