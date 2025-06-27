# ---------------------- Desafio 009 ----------------------
# Questão: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

num = int(input('Informe um número: '))


# Optei por o formato de exibição com "print(f'')" do que utilizar o ".format()", pois iria repetir varias vezes a variável "num"
print(f' {'-'*20}\n {num} x 1 = {num*1}\n {num} x 2 = {num*2}\n {num} x 3 = {num*3}\n {num} x 4 = {num*4}\n {num} x 5 = {num*5}\n {num} x 6 = {num*6}\n {num} x 7 = {num*7}\n {num} x 8 = {num*8}\n {num} x 9 = {num*9}\n {num} x 10 = {num*10}\n {'-'*20}')

# Feito de uma forma mais automatizada:
# x = 1
# while x <= 10 :
#     print('{} x {} = {}'.format(num, x, num*x))
#     x += 1