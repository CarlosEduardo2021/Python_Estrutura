nome = str(input('Qual seu nome? '))
if nome == 'jhon':
    print('Nome correto !')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Tente novamente !')
elif nome in 'Ana  Joana Mardos Aparecido':
    print('Nomes cadastrados')
else:
    print('Nome incorreto !')
print('Tenha um bom dia {} !' .format(nome))