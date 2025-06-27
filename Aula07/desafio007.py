# ---------------------- Desafio 007 ----------------------
# Questão: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média 

#A questão não pediu mais optei por adicionar uma verificação para que não fosse possível colocar valores abaixo de 0 e nem acima de 10, assim fiz um while e com duas verificações, para sair somente do mesmo quando o número digitado for entre 0 e 10. 

status1 = True

status2 = True

nota1 = float(input('Informe a primeira nota: '))

while(status1):
    if ((nota1 < 0) or (nota1 > 10)) :
        print('Nota 1 inválida!')
        nota1 = float(input('Informe a nota 1 válida: '))
        
    if ((nota1 >= 0) and (nota1 <= 10)):
        status1 = False

nota2 = float(input('Informe a segunda nota: '))

while(status2):
    if ((nota2 < 0) or (nota2 > 10)):
        print('Nota 2 inválida!')
        nota2 = float(input('Informe a nota 2 válida: ')) 

    if ((nota2 >= 0) and (nota2 <= 10)):
        status2 = False


media = (nota1 + nota2) / 2

# Coloquei somente para aparecer duas casas decimais após a virgula 
print('Média: {:.1f}'.format(media))