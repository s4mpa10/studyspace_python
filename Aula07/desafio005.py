# ---------------------- Desafio 005 ----------------------
# Questão: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor 

num = int(input('Informe um número: '))

# Para calcular o antecessor é necessário pegar o número que o usuário digitou o subtrair um
antecessor = num - 1 

# Para calcular o sucessor é necessário pegar o número que o usuário digitou o somar um
sucessor = num + 1

print(' Número antecessor = {}\n Número sucessor = {}'.format(antecessor, sucessor))