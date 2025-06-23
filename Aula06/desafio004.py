# ---------------------- Desafio 003 ----------------------
# Questão: Fça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. 

valor = input('Digite algo no teclado: ')
print(f'Você esvreveu: {valor}')
print(f'O tipo que você digitou: {type(valor)}')
print(f'Ele é alfanumerico? {valor.isalnum()}')
print(f'Ele é um texto? {valor.isalpha()}')
print(f'Ele é numerico? {valor.isnumeric()}')
print(f'Ele é MAIUSCULO? {valor.isupper()}')
print(f'Ele é minusculo? {valor.islower()}')
print(f'Possui espaço no texto digitado? {valor.isspace()}')
print(f'O texto é impresso? {valor.isprintable()}')
print(f'Ele é um digito? {valor.isdigit()}')

# Informação:
# Se valor for ' ', valor.isspace() retornará True.
# Se valor for ' \t\n', valor.isspace() também retornará True.
# Se valor for 'Olá mundo', valor.isspace() retornará False (porque contém letras).
# Se valor for '' (uma string vazia), valor.isspace() retornará False.
