lista = []
dimensao = int(input("quantos numeros voce quer somar? "))
soma = int(0)
numeros = int(0)
#criar lista
for vezes in range (dimensao):
    numeros = int(input("quais numeros voce quer somar? "))
    lista.append(numeros)
    print(vezes)
#somar lista
for i in range (len(lista)):
    soma = lista[i] + soma
print(lista)
print(soma)