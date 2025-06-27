# ---------------------- Desafio 011 ----------------------
# Questão: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
# Área (m²) = Altura (m) x Largura (m) 

# Entendimento:
#  1L  = 2m²
#  XL  = 100m²
# XL = 100/2
# XL = 50L

altura = float(input('Informe a altura em metros: '))

largura = float(input('Informe a largura em metros: '))

area = altura * largura

qtd_tinta = area / 2

print(' Área (m²) = {}\n Precisa de {:.1f}L de tinta para pintar toda a área da parede.'.format(area, qtd_tinta))

