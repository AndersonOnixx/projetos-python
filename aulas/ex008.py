m = float(input("Digite um numero em metros:"))
km = m / 1000
hm = m / 100
dm = m / 10
cm = m * 10
dcm = m * 100
mm = m * 1000
print("A medida de {}m correspote a:" .format(m))
print("Valor em km: {}\nValor em hm: {}\nValor em dm: {}" .format(km, hm, dm))
print("Valor em cm: {}\nValor em dcm: {}\nValor em mm: {}" .format(cm, dcm, mm))