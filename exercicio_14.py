opcao = int(input('Escolha uma opção: \n1 - Converter km/h em m/s \n2 - Converter m/s em km/h \n3 - Parar o programa \n'
                  'Digite sua opção: '))

while 1 <= opcao <= 3:
    if opcao == 1:
        km = float(input('Informe a velocidade em km/h: '))
        print(f' A velocidade em metros/segundo é: {km / 3.6:.2f}')

    elif opcao == 2:
        ms = float(input('Informe a velocidade em metros por segundo: '))
        print(f' A velocidade em quilômetros/hora é: {ms * 3.6:.2f}')

    elif opcao == 3:
        break

    opcao = int(input('Escolha uma opção: \n1 - Converter km/h em m/s \n2 - Converter m/s em km/h \n'
                      '3 - Parar o programa \nDigite sua opção: '))
