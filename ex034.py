#escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salarios superiores a R$1.250,00 calcule um aumento de 10%
#para os inferiores ou iguais o aumento é de 15%
salario = float(input('Qual é o salario do funconario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,novo))