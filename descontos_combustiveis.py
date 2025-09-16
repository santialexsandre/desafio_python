print('  ** CALCULADORA DESCONTO COMBUSTÍVEL  **')
#MENU DE ESCOLHA
print('  ** SELECIONE [E] - ETANOL [D] - DIESEL  **')
#ENTRADA DO MENU
escolha = (input('COMBUSTIVEL: ')).upper()
#VARIAVEIS ATRIBUIDAS PARA ARMAZENAR OS VALORES
valor_litro_etanol = 1.70
valor_litro_diesel = 2.00

#CONDIÇÃO ETANOL
if escolha == 'E':
   litro = float(input('Digite a QTDE em litros: '))
   #SE A QUANTIDADE EM LITROS FOR INFERIOR OU IGUAL A 15 LITROS
   if litro <= 15:
    valor_total =  litro * valor_litro_etanol * 0.98 #2% de desconto
     #SE A QUANTIDADE EM LITROS FOR SUPERIOR A 15 LITROS
   else:
     valor_total =  litro * valor_litro_etanol * 0.96 #4% de desconto
#CONDIÇÃO DIESEL
elif escolha == 'D':
  litro = float(input('Digite a QTDE em litros: '))
  #SE A QUANTIDADE EM LITROS FOR INFERIOR OU IGUAL A 15 LITROS
  if litro <= 15:
    valor_total =  litro * valor_litro_diesel * 0.97 #3% de desconto
    #SE A QUANTIDADE EM LITROS FOR SUPERIOR A 15 LITROS
  else:
     valor_total =  litro * valor_litro_diesel * 0.95 #5% de desconto
else:
  print('Valor inválido!')
  exit()

#RETORNAR O VALOR A SER PAGO DO CLIENTE APÓS CALCULO DE DESCONTO E LITRAGEM 
print(f'O valor a ser pago é de: {valor_total:.2f}')