salario = float(input('Qual é o seu salario? R$'))
novo = salario+(salario*15/100)
print('Seu salario que era de R${:.2f}, com 15% de aumento, subiu para R${:.2f}'.format(salario, novo))

