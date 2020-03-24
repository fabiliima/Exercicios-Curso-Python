with open('arq.txt', 'a', encoding='utf-8') as arquivo:
    with open('arq.txt') as arquivo:
        print(arquivo.read())
    while True:
        texto = input('Informe um conteúdo para o arquivo ou digite 0 para sair: ')
        if texto != '0':
            arquivo.write(texto + '\n')
        else:
            break
