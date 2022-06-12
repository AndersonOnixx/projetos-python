print('\t' * 3 + 'ORGANIZAÇÕES TABAJARA')
print('_' * 72)

print('|\tReajuste baseado no salário atual                                  |')
print('_' * 72)
print('|\t- salários até R$ 280,00 (incluindo)       |   aumento de 20%      |\n'
      '|\t- salários entre R$ 280,00 e R$ 700,00     |   aumento de 15%      |\n'
      '|\t- salários entre R$ 700,00 e R$ 1500,00    |   aumento de 10%      |\n'
      '|\t- salários de R$ 1500,00 em diante :       |   aumento de 5%       |')
print('_' * 72)

salario = float(input('Informe seu salario atual: '))

if (salario < 281):
    percentual = 20
    valorAumento = salario * 0.2
    novoSalario = salario + valorAumento
elif(salario > 280 and salario < 700):
    percentual = 15
    valorAumento = salario * (15/100)
    novoSalario = salario + valorAumento
elif(salario > 700 and salario < 1500):
    percentual = 10
    valorAumento = salario * (10/100)
    novoSalario = salario + valorAumento
else:
    percentual = 5
    valorAumento = salario * (5/100)
    novoSalario = salario + valorAumento

print('O salário antes do reajuste:         R$ {:.2f}' .format(salario))
print('O percentual de aumento aplicado:    {}%' .format(percentual))
print('O valor do aumento:                  R$ {:.2f}' .format(valorAumento))
print('O novo salário, após o aumento:      R$ {:.2f}' .format(novoSalario))
