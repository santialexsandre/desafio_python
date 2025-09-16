print(' ** ANÁLISE DE VENDAS **')

vendas_2022 = float(input('Valor de vendas em 2022: '))
vendas_2023 = float(input('Valor de vendas em 2023: '))

variacao = ((vendas_2023 - vendas_2022) / vendas_2022) * 100

if variacao > 20:
    print('Bonificação para a equipe de vendas!')
elif 2 <= variacao <= 20:
    print('Pequena bonificação para a equipe de vendas!')
elif -10 <= variacao <= 2:
    print('Planejamento de políticas de incentivo às vendas')
elif variacao <= -10:
    print('Corte de gastos!')

print(f'A variação é de {variacao:.2f}%')