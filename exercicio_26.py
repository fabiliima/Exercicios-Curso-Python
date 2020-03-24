def media(nota1, nota2, nota3, letra):
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    nota3 = float(input('Informe a terceira nota: '))
    letra = (input('Digite "A" para calcular a média aritmética. \nDigite "B" para calcular a média ponderada. '
                   '\nDigite '
                   'sua opção: '))
    if letra.upper() == "A":
        return (nota1 + nota2 + nota3) / 3
    return (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10


print(f'O cálculo da média é: {(media("nota1", "nota2", "nota3", "letra")):.2f}')
