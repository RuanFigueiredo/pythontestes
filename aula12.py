#estrutura condicional aninhada
nome = str(input('Qual é o seu nome?'))
if nome == 'Ruan':
    print('\n Que nome legal, eu gostei ein!')
elif nome == 'Maria' or nome == 'João' or nome == 'Pedro':
    print('\n Seu nome é bem popular')
elif nome in 'Jubileu Estomazildo Jébio drauziomino':
    print('\n Seu nome está entre os mais bizarros do brasil, parabéns!')
else:
    print('\n Seu nome é diferente, mas não é popular')
print('\n tenha um bom dia, {}!'.format(nome))
