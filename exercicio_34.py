def duas_strings(str1, str2):
    str1 = input('Informe a primeira palavra ou frase: ')
    str2 = input('Informe a segunda palavra ou frase: ')

    lista = [i + j for i, j in zip(str1, str2)]  # concatenar as duas palavras letra por letra, em uma lista
    for n in lista:  
        str1 += n
    return str1


print(duas_strings('str1', 'str2'))
