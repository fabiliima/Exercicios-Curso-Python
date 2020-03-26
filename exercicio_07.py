preco_novo = 0
preco_antigo = float(input('Informe o preço antigo do produto: R$ '))

if preco_antigo > 100:
    preco_novo = preco_antigo * 1.15

elif preco_antigo >= 50 and preco_antigo <= 100:
    preco_novo = preco_antigo * 1.10

else:
    preco_novo = preco_antigo * 1.05
    
    
if preco_novo > 200:
    print(f'{preco_novo:.2f}')
    print('Muito Caro')

elif preco_novo > 120 and preco_novo <= 200:
    print(f'{preco_novo:.2f}')
    print('Caro')

elif preco_novo >= 80 and preco_novo <= 120:
    print(f'{preco_novo:.2f}')
    print('Normal')

else:
    print(f'{preco_novo:.2f}')
    print('Barato')
