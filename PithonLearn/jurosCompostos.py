c = int(input('Valor das capital inicial:R$ '))
taxa = int(input('Taxa de rendimento % ao ano"): '))
anos = int(input('Quantos de investimento: '))

montante = int ((c * (1 + (taxa / 100)))**anos)

print('Para uma envestimento de R${:.2f} em {} anos'.format(c, anos), end='')
print(' o valor final será de R$ {}'.format(montante))