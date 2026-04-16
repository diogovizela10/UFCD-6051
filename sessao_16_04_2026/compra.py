#ciclo principal
while True:

    #Dados de entrada

    stock  = 30
    pagamento = True

    #Processamento

    if pagamento == True and stock > 0:
        print("Compra efetuada com sucesso!")
        imprimir_Fatura = True
    else:  
      print("Stock insuficiente ou pagamento não efetuado!")
      imprimir_Fatura = False
     
     #Dados de saída 