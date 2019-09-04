#Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preco
#da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
ditancia = float(input('Qual a distancia da sua viagem?'))
if distancia > 80:
    print('MULTADO! Voce excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80)*7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com seguranca!')