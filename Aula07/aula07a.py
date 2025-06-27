# ---------------------- Aula 07 - Operadores Aritméticos ----------------------

# Soma (+)
print(f'Soma: 5 + 2 == 7? {5+2==7}')

# Subtração (-)
print(f'Subtração: 5 - 2 == 3? {5-2==3}')

# Multiplicação (*)
print(f'Multiplicação: 5 * 2 == 10? {5*2==10}')

# Divisão (/)
print(f'Divisão: 5 / 2 == 2.5? {5/2==2.5}')

# Potência (**)
print(f'Potência: 5 ** 2 == 25? {5**2==25}')

# Divisão inteira (//)
print(f'Divisão Inteira: 5 // 2 == 2? {5//2==2}')

# Resto da Divisão(%)
print(f'Resto da Divisão: 5 % 2 == 1? {5%2==1}')

# Exemplo utilizado na aula: 

num1 = int(input('Um valor: '))
num2 = int(input('Outro valor: '))
soma = num1 + num2
mult = num1 * num2
div = num1 / num2
divI = num1 // num2
exp = num1 ** num2

# O ", end=' '" server para não quebrar a linha com o pródimo print 

# Já o "\n" server para quebrar a linha , quando necessário

print('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(soma, mult, div), end=' ')

print('Divisão inteira {} e potência {}'.format(div, divI))