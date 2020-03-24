def operacoes_matematicas(num1, num2, simbolo):
    num1 = float(input('Informe o primeiro número: '))
    num2 = float(input('Informe o segundo número: '))
    simbolo = (input('Para adição, digite: + \nPara subtração, digite: - \nPara multiplicação, digite: *\nPara divisão,'
                     'digite: /\nDigite sua opção: '))
    if simbolo == '+':
        return f'A soma é: {num1 + num2}'
    elif simbolo == '-':
        return f'A subtração é: {num1 - num2}'
    elif simbolo == '*':
        return f'A multiplicação é: {num1 * num2}'
    return f'A divisão é: {num1 / num2}'


print(operacoes_matematicas('num1', 'num2', 'simbolo'))
