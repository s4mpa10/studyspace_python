# ---------------------- Uso da função input(): ----------------------
# 1. Com os conhecimentos de variáveis, agora será utilizado a função input() para receber do usuário valores relacionados as variáveis

# A variável 'nome' através do input recebe um valor adicionado pelo usuário com sua interação
nome = input('Qual é o seu nome? ')

# A variável 'idade' através do input recebe um valor adicionado pelo usuário com sua interação, não sendo necessáriamente um valor inteiro, pois não foi declarado isso
idade = input('Quantos anos você tem? ')

# A variável 'peso' através do input recebe um valor adicionado pelo usuário com sua interação, não sendo necessáriamente um valor float, pois não foi declarado isso
peso = input('Quanto você pesa? ')

# Para exitir essas informações todas juntas é necessário utilizar a "," e não o operador "+", pois estamos seperando e utilizando variáveis com tipos diferentes 
print(nome, idade, peso)