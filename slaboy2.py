nome = str(input('digite seu nome completo')).strip()
print('seu nome comeca com {} e termina com {}'.format(nome.find(" "), nome.rfind(" ")+1))