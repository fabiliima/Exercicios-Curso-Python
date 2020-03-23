meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro',
       # 11
       'dezembro')
mes = int(input('Informe um número de 1 á 12: '))

if mes >= 1 and mes <= 12:
    print(
        f' Este mês é {meses[mes - 1]}.')  
else:
    print('Número inválido.')
