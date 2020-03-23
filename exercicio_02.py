dia_da_semana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
dia = int(input('Informe um número de 1 á 7: '))

if dia >= 1 and dia <=7:
    print(f' Hoje é {dia_da_semana[dia - 1]}.')  
else:
    print('Número inválido.')
