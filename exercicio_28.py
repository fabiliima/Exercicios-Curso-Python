def soma_intervalo(num1, num2):
    soma = 0
    num1 = int(input('Informe um número inteiro e positivo: '))
    num2 = int(input('Informe um número inteiro e positivo: '))
    while num1 < 0:
        num1 = int(input('Informe um número inteiro e positivo: '))
    while num2 < 0:
        num2 = int(input('Informe um número inteiro e positivo: '))
    for n in range(num1, num2+1):
        soma += n
    return f'A soma dos números no intervalo entre {num1} e {num2} é: {soma}'


print(soma_intervalo('num1', 'num2'))
