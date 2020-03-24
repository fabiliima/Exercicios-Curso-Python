def anagrama(palavra1, palavra2):
    palavra1 = input('Informe a primeira palavra: ')
    palavra2 = input('Informe a segunda palavra: ')

    n1 = len(palavra1)  # n1 e n2 recebem um número equivalente ao tamanho de cada palavra
    n2 = len(palavra2)

    if n1 != n2:  # se forem tamanhos diferentes, já não são anagramas
        return 'As palavras possuem tamanhos diferentes, portanto não são anagramas.'

    palavra1 = sorted(palavra1)  # p1 e p2 agora estão ordenadas em ordem alfabética
    palavra2 = sorted(palavra2)

    for i in range(0, n1):
        if palavra1[i] != palavra2[i]:  # se no indice, não possuirem a mesma letra, não são anagramas
            return f'As palavras não possuem as mesmas letras, portanto não são anagramas.'

    return 'As palavras são anagramas.'


print(anagrama('palavra1', 'palavra2'))
