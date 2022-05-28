
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
q = int(input("Quantidade de dias:"))
km = float(input("Quantidade de km:"))
c = (q * 60) + (km * 0.15)
print("Valor do parcamento: R${:.2f}" .format(c))
#inheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
r = float(input("Valor em real:R$"))
v = r / 3.27
print("Valor em dólar: {:.2f}$" .format(v))
#Faça um programa que leia a largura e a altura de uma parede em metros,nta necessária para pintá-la, sabendo que cada litro
l = float(input("Largura da parete:"))
a = float(input("Altura da parete:"))
v = (a * l) / (2)
print("Valor petido em largura e Altura: {}largura e {}Altura\nvalor: {}L" .format(l, a, v))
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input("Qual o preço do protudo:"))
v = (p * 5) / (100)
s = p - v
print("Valor de protudo: {}\ndesconto de 5%\nValor: {}" .format(p, s))
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input("Qual o seu salario:"))
ds = (s * 15) / (100)
v = ds + s
print("Valot de seu salario: {}\nVai receber o almento de 15%\nValor do almento: {:.1f}" .format(s, v))
"""
