l = float(input("Digite a largura:"))
a = float(input("Altura da parede:"))
d = (l * a)
l = ( d *1000 ) / ( 2 )
print("Sua parede tem a timenção de  {}x{} e a sua area é de {}m²" .format(l, a, d))
print("Para voce pintar as paredes voce precisa de {}L" .format(l))