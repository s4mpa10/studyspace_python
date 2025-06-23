# ---------------------- Aula 06 - Tipos primitivos ----------------------

# Analisando os tipos:

# # Identificando o tipo 'string'
# # O que ocorre aqui é, o valor que eu digitar, seja numero ou seja um texto, sempre vai ser reconhecido como texto
# valor = str(input('Digite um valor: '))

# # Identificando o tipo 'int'
# # O que valor que digitar aqui está relacionado com uma atribuição exclusivamente de valores inteiros, seja positivo ou negativo
# valor = int(input('Digite um valor: '))

# # Identificando o tipo 'float'
# # O que é reconhecido aqui com o float, está relacionado com valores com virgulas, sejam negativos ou postivos, podendo receber também valores interior, mas que são reconhecimento dessa forma: 9.0
# valor = float(input('Digite um valor: '))

# # Identificando o tipo 'bool'
# # Já o valor booleano, somente tem duas atribuições, ou é Verdadeiro(True) ou é Falso(False) 
# valor = bool(input('Digite um valor: '))


# Existe a função is() no python que ela é nativa e abrange a necessidade de realização de if e else, sendo realizado possibilidades para saber se um valor é numerico ou não, quando não é definido o tipo no momento do input
# A resposta estará de acordo com o valor que o usuário vai digitar, que no exemplo abaixo está sendo digitado com um valor númerico 
# Exemplo: 
# valor = input("Digite um valor: ")
# print(valor.isnumeric())

# Agora está sendo demonstrado o isalpha(), dando destaque para saber se pode ser convertido para texto(string) ou não, a resposta é em formato booleano
# Exemplo: 
valor = input("Digite um valor: ")
print(valor.isalpha())

# Testa para saber se a conversão é alfanumerico ou não, a resposta é em formato booleano
# Exemplo: 
valor = input("Digite um valor: ")
print(valor.isalnum())