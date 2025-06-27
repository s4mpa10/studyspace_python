# ---------------------- Desafio 012 ----------------------
# Questão: Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, como 5% de desconto.

# A lógica de resolução ocorre primeiro para calcular o desconto, e depois subtrair do valor total digitado pelo usuário.
# 5% = 5/100 = 0.05

valor = float(input('Digite o preço do produto: '))

desconto = valor * 0.05

valor = valor - desconto

print('Desconto de 5%: {:.2f} \nPreço atualizado: R$ {:.2f}'.format(desconto, valor))