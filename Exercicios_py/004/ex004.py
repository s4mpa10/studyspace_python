# ---------------------- Exercício 03 ----------------------
# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ela.

valor = input('Digite algo no teclado: ')

print(f'O tipo primitivo desse valor é: {type(valor)}')
print(f'Só tem espaços? {valor.isspace()}')
print(f'É um número? {valor.isnumeric()}')
print(f'É alfabético? {valor.isalpha()}')
print(f'É alfabumérico? {valor.isalnum()}')
print(f'Está em maiúsculas? {valor.isupper()}')
print(f'Está em minúsculas? {valor.islower()}')
print(f'Está centralizada? {valor.istitle()}')