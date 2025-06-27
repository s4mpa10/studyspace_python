# ---------------------- Desafio 006 ----------------------
# Questão: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada 

num = int(input('Digite um número: '))

# Para realizar as multiplicações, criei uma variável para cada, destacando o que era necessário e utilizei a raiz quadrada que foi apresentado na aula, por meio: **(1/2)
dobro = num * 2

triplo = num * 3

raiz_quadrada = pow(num,(1/2))
# Pode ser assim também num**(1/2)

print(' Dobro do número: {}\n Triplo do número: {}\n Raiz quadrada: {:.2f}'.format(dobro, triplo, raiz_quadrada))