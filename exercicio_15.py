opcao = int(input('Escolha uma opção: \n1 - Para adição; \n2 - Subtração; \n3 - Multiplicação; \n4 - Divisão; \n'
                  '5 - Saída \nDigite sua opção: '))

while 1 <= opcao <= 4:

    num1 = float(input('Informe o primeiro número: '))
    num2 = float(input('Informe o segundo número: '))

    if opcao == 1:
        print(f'A soma é: {num1 + num2}')

    elif opcao == 2:
        print(f'A subtração é: {num1 - num2}')

    elif opcao == 3:
        print(f'A multiplicação é: {num1 * num2}')

    elif opcao == 4:
        print(f'A divisão é: {num1 / num2}')

    opcao = int(input('Escolha uma opção: \n1 - Para adição; \n2 - Subtração; \n3 - Multiplicação; \n4 - Divisão; \n'
                      '5 - Saída \nDigite sua opção: '))
while opcao == 5:
    break
