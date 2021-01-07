# Exercico 36
# Emprestimo bancario, valor, salario, não pode exeder 30% do salario.

casa = float(input('Valor das casa:R$ '))
salario = float(input('Salario do comprador:R$ '))
anos = int (input('Quantos anos de financiamemto:R$ '))
prestação = casa / ( anos * 12)
minimo = salario * 30 /  100
print('Para pagas uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser concedido!')
else:
    print('Empréstimo negado!')