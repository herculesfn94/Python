preco = float(input('Qual o preco do produto? R$ '))
novo = preco - (preco*5 / 100)
print('O pruduto que custava R${:.2f}, com 5% de desconto vai custar R${:.2f}'.format(preco, novo))