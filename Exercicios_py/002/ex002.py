# ---------------------- Exercício 02 ----------------------
# Questão: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas

nome = str(input('Digite o seu nome: '))

# No python existe a formatação que fica dentro dos "{}". Assim, destaco que o que tenho na variável "nome" caberá na saída "{}"
print(f'É um prazer te conhecer, {nome}!')

# Outra forma de adicionar o print formatado, é assim:
# print('É um prazer te conhecer, {}!'.format(nome))