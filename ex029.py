#escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80km/h, mostre a mensagem
#dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.
velocidade = float(input('Qual a velocidade atual do carro?'))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80)*7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com seguranca!')

