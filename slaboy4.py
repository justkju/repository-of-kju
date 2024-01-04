v = float(input('digite uma velocidade: '))

if v > 80:
    print('voce foi multado!')
    print('sua multa foi de {:.2f} reais!'.format((v-80)*7))
else:
    print('voce nao foi multado, boa viagem!')