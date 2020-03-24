with open('arq.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        texto = input('Informe um conteúdo para o arquivo ou digite 0 para sair: ')
        if texto != '0':
            arquivo.write(texto + '\n')
        else:
            break

char = input('Informe uma letra ou número: ')

with open('arq.txt') as arquivo:
    contador = [caracter for caracter in arquivo.read() if caracter.lower() == char.lower()]
    print(f'O caracter {char} aparece {len(contador)} vezes no arquivo.')
