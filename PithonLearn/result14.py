# Escolha a base de conversão

num = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão:
[1] converter para BINÁRIO
[2] convertere para OCTAL
[3] converter para HEXADECIMAL''')
opção = int (input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual {} '.format(num, bin(num)[2:])) 
elif opção == 2:                                                                 
    print('{} convertido para OCTA é igual a {} '.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {} '.format(num, hex(num)[2:]))
else:
    print('Opção invalida, Tente novamente.')
# O [2:], presente aqui e nos outros, se refere ao fatiamento de string, no caso os dois 
# primeiros não vão aparecer, ex. 125 binario é 0b1111101 com o [2:] fica 1111101 .