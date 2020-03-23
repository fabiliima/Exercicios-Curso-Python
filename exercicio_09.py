custo_fabrica = float(input('Qual o custo de fábrica do carro? '))

if custo_fabrica < 12_000:
    comissao_distribuidor = custo_fabrica * 0.05
    impostos = 0
    print(f'O custo para o consumidor é: R$ {custo_fabrica + comissao_distribuidor + impostos:.2f}')
    
if custo_fabrica > 12_000 and custo_fabrica <= 25_000:
    comissao_distribuidor = custo_fabrica * 0.10
    impostos = custo_fabrica * 0.15
    print(f'O custo para o consumidor é: R$ {custo_fabrica + comissao_distribuidor + impostos:.2f}')
    
if custo_fabrica > 25_000:
    comissao_distribuidor = custo_fabrica * 0.15
    impostos = custo_fabrica * 0.20
    print(f'O custo para o consumidor é: R$ {custo_fabrica + comissao_distribuidor + impostos:.2f}')

