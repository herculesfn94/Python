#crie um programa que leia o nome completo de uma pessoa e moste:
#o nome com todas as letras maiusculas e minusculas.
#Quantas letras ao #todo(semconsiderar espacos)
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome....')
print('Seu nome em letras maiusculas é {}'.format(nome.upper()))
print('Seu nome em letra minuscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

