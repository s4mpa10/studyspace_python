# ---------------------- Exercício 03 ----------------------
# Questão: Crie um programa que leia dois números e mostre a soma entre eles.

num1 = int(input('Digite um valor: '))

num2 = int(input('Digite outro valor: '))

soma = num1 + num2

print(f'A soma entre {num1} e {num2} é igual a {soma}!')

# Pode ser feito assim também, utilizando o ".format()": 
# print('A soma entre {} e {} é igual a {}'.format(num1, num2, soma))
