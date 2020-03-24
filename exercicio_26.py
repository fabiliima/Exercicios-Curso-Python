def media(nota1, nota2, nota3, letra):
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    nota3 = float(input('Informe a terceira nota: '))
    letra = (input('Digite "A" para calcular a média aritmética. \nDigite "P" para calcular a média ponderada. '
                   '\nDigite '
                   'sua opção: '))
    if letra.upper() == "A":
        return f'O cálculo da média é: {nota1 + nota2 + nota3 / 3:.2f}'
    elif letra.upper() == "P":
        return f'O cálcula média é: {nota1 * 5 + nota2 * 3 + nota3 * 2 / 10:.2f}'
    else:
        "Letra não corresponde as opções."


print(media("nota1", "nota2", "nota3", "letra"))
