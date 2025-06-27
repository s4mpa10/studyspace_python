# ---------------------- Desafio 008 ----------------------
# Questão: Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros 

# Transformações da esquerda para a direita multiplica por 10 (x10): 
# KM --> HM --> DAM --> M --> DM --> CM --> MM

# Transformações da direita para a esquerda dividi por 10 (/10): 
# KM <-- HM <-- DAM <-- M <-- DM <-- CM <-- MM

valor = float(input('Informe o valor em metros: '))

converter_cm = valor * 100

converter_mm = valor * 1000

print(' Centimetros: {}cm\n Milimetros: {}mm'.format(converter_cm, converter_mm))