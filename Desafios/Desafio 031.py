#perguntar a distancia de uma viagem em km
#calcular passagem cobrando 0,50 por km em até 200km
#calcular passagem corando 0,45 por km acima de 200km
viagem=float(input('Qual a distância da sua viagem: '))
if viagem<=200.0:
    valor=viagem*0.5
    print('Por essa distância, cada Km será cobrado R$0,50')
    print('O valor da sua viagem será de: R${:.2f}'.format(valor))
else:
    valor=viagem*0.45
    print('Por essa distância, cada Km será cobrado R$0,45')
    print('O valor da sua viagem será de: R${:.2f}'.format(valor))