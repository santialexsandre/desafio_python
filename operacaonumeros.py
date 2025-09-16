print(' ***   OPERAÇÃO DE DOIS NÚMEROS E CLASSIFICAÇÃO   ***')

#Solitia ao usuario dois números
number_1 = float(input('Digite um número: '))
number_2 = float(input('Digite outro número: '))

#Solicita ao usuario uma operação +, -, *, / e aloca em uma variavel chamada operador
print('\n (+) Soma | (-) Subtração | (*) Multiplicação | (/) Divisão')
operador = str(input('Digite uma operação a ser feita: '))

#Calculadora de operação
if operador == '+':
    resultado = number_1 + number_2
    print(f'A soma é = {resultado}')
elif operador == '-':
    resultado = number_1 - number_2
    print(f'A subtração é = {resultado}')
elif operador == '*':
    resultado = number_1 * number_2
    print(f'A multiplicação é = {resultado}')
elif operador == '/':
    resultado = number_1 // number_2
    print(f'A divisão é = {resultado}')

#Operação de resto para identificar se o número é par ou impar, se o resto for '0' é PAR e se for '1' é impar
if resultado == 0:
    print(f'É um número NEUTRO')
elif resultado % 2 == 0:
    print(f'É um número PAR')
else:
    print(f'É um número IMPAR')

#Avalia se o valor ficou acima ou inferior a '0' se for acima é positivo e se for abaixo é negativo se for '0' é neutro.
if resultado > 0:
    print('Ele é um número POSITIVO')
elif resultado < 0:
    print('Ele é um número NEGATIVO')
else:
    print('Ele é um número NEUTRO')

if resultado % 1 == 0:
    print('Ele é um número INTEIRO')
else:
    print('Ele é um número DECIMAL')