# ---------------------- Desafio 013 ----------------------
# Questão: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# A lógica de resolução ocorre primeiro para calcular o aumento, e depois pega o valor do salário que o usuário digitou e soma com o aumento.
# 15% = 15/100 = 0.15

salario = float(input('Informe o seu salário: '))

aumento = salario * 0.15

salario = salario + aumento

print(' Aumento de 15%: {:.2f}\n Novo salário: {:.2f}'.format(aumento, salario))