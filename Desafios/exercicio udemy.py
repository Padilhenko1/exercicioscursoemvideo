meses=('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
dia_nasc= str(input('Qual a sua data de nascimento [DD-MM-AAAA]: '))
'''dia_nasc=int(input('Dia: '))
mes_nasc=int(input('Mês: '))
ano_nasc=int(input('Ano: '))
mes=meses[mes_nasc-1]'''
mes=int(dia_nasc[3:5])
mes=meses[mes-1]
print(f'Você nasceu no mês de {mes}.')

