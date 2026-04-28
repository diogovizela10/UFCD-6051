#ciclo principal

while True:
    #dados de entrada

    vendas_segunda = 1
    vendas_terca = 2
    vendas_quarta = 100
    vendas_quinta = 1
    vendas_sexta = 100
    vendas = [vendas_segunda, vendas_terca, vendas_quarta, vendas_quinta, vendas_sexta]
    numerodias = 5

#estrutura de dados -> lista

    media = [1,2,100,1,100]


    print ("A média de vendas da semana é: ", media, "euros")
    #verificar se o dia foi bom
    if vendas_segunda - media > 0:
        print ("As vendas de segunda-feira estão acima da média")
    else:
         print ("As vendas de segunda-feira estão abaixo da média")

    if vendas_terca - media > 0:
            print ("As vendas de terça-feira estão acima da média")
    else:
            print ("As vendas de terça-feira estão abaixo da média")

    if vendas_quarta - media > 0:
        print ("As vendas de quarta-feira estão acima da média")
    else:
        print ("As vendas de quarta-feira estão abaixo da média")
    if vendas_quinta - media > 0:       

        print ("As vendas de quinta-feira estão acima da média")   
    else:
        print ("As vendas de quinta-feira estão abaixo da média")
    if vendas_sexta - media > 0:
        
        print ("As vendas de sexta-feira estão acima da média") 
    else:
        print ("As vendas de sexta-feira estão abaixo da média")       

    
