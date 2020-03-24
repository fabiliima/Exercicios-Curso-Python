altura_c = 1.50
altura_z = 1.10
ano = 0

while altura_z < altura_c:
    altura_c += 0.02
    altura_z += 0.03
    ano += 1
if altura_z >= altura_c:
    print(f'A altura do Zé é: {altura_z:.2f}')
    print(f'A altura do Chico é: {altura_c:.2f}')
    print(f'Demorou {ano} anos.')
