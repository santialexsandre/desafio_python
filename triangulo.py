print ('** FORMAÇÃO DE TRIÂNGULO  **')

lado_a = int(input('Digite o valor do lado A: '))
lado_b = int(input('Digite o valor do lado B: '))
lado_c = int(input('Digite o valor do lado C: '))

if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
    print('É um triângulo!')
    if lado_a == lado_b == lado_c:
        print('É um Triângulo Equilátero')
        
    elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
        print('É um Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Não é possível formar um triângulo!')

