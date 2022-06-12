valo=int(input("digite uma porcentagem:"))
if(valo>10)and(valo<19):
    print("Refresco")
else:
    if( (valo>10)and(valo<50)):
        print("Nectar")
    else:
        if(valo<=10):
                print("Água saborizada")
        else:
            if(valo>50)and(valo<100):
                print("Suco")
            else:
                if(valo>100):
                    print("ERROR!!!")