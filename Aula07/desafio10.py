# ---------------------- Desafio 010 ----------------------
# Questão: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.  Considere: US$ 1,00 = R$5,48 (Peguei a cotação atual)

# Para resolver a questão basta realizar uma regra de 3, pegando o valor que o usuário tem na carteira e dividindo pelo valor do dólar especificado

# Exemplo:
# US$ 1,00 = R$5,48
#    X     = R$100,00
# X = 100/5.48
# X = US$ 18.24

valor = float(input('Digite a quantidade de dinheiro que tem na carteira: '))

v_dolar = valor / 5.48

print('Com R$ {:.2f} você pode comprar US$ {:.2f} nos Estados Unidos.'.format(valor, v_dolar))
