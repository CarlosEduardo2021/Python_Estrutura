# Valor de juros compostos para investimento anual.

c = float(input('Valor do capital inicial:R$ '))
taxa = float(input('Taxa em % de rendimento ao ano: '))
anos = int(input('Investimento de quantos anos : '))

montante = int (c * ((1 + (taxa / 100))**anos))
lucro = float (montante - c)

print('Para uma envestimento de R${:.2f} por {} anos'.format(c, anos), end='')
print(' o seu lucro é de R$ {:.2f} , resultando no total de {:.2f} '.format(lucro, montante))