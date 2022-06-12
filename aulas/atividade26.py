#atividade26
print("_" * 72)
print("\t" *7+ 'TABELA DE DESCONTO')
print("_" * 72)
print(" -------------------------------ÀLCOOL---------------------\n"
      "|\t- 20 litros:                   |   desconto de 3%     |\n"
      "|\t- Acima de 20 litros:          |   desconto de 5%     |\n"
      "|\t --------------------------GASOLINA-------------------|\n"
      "|\t- 20 litros:                   |   desconto de 4%     |\n"
      "|\t- Acima de 20 litros :         |   desconto de 6%     |")
print("-"*59)
print("_" * 72)
combustve = str(input("Qual o tipo de combustve:"))
litro = float(input("Quantidade de Litros:"))
if((combustve == "Alcool")and(litro <= 20)):
    print("Tipo de combustve é Álcool")
    percentual = 3
    calculo1 = 2.50 * litro
    calculo2 = calculo1 - 0.03
elif((combustve == "Alcool")and(litro > 20)):
    print("Tipo de combustve é Álcool")
    percentual = 5
    calculo1 = 2.50 * litro
    calculo2 = calculo1 - 0.05
elif((combustve == "Gasolina")and(litro <= 20)):
    print("Tipo de combustve é Gasolina")
    percentual = 4
    calculo1 = 1.90 * litro
    calculo2 = calculo1 - 0.04
elif((combustve == "Gasolina")and(litro > 20)):
    print("Tipo de combustve é Gasolina")
    percentual = 6
    calculo1 = 1.90 * litro
    calculo2 = calculo1 - 0.06
print("O percentual de desconto aplicado:{}%" .format(percentual))
print("Valor a pagar:{:.2f}R$".format(calculo2))