#ciclo inicial

posicaojanela1= 5  #valor pode ir a 90º
posicaojanela2= 5  #valor pode ir a 90º

while True:
    #dados de entrada

    janela1_cima= True #botao janela 1 cima 
    janela1_baixo= False #botao janela 1 baixo 
    janela2_cima= False #botao janela 2 cima 
    janela2_baixo= False #botao janela 2 baixo 

    

    #processamento

    if janela1_cima == True and posicaojanela1 <= 90:
      posicaojanela1 =  posicaojanela1 + 1 
      print (" A posicao da janela 1 atual é : ", posicaojanela1)

      #botao janela 1 cima (sobe 1 grau máximo 90)

      
    else: 
       if janela1_baixo == True and posicaojanela1 >= 0:
            posicaojanela1 = posicaojanela1 -1
            print (" A posicao da janela 1 atual é : ", posicaojanela1)
            #botao janela 1 baixo (desce 1 grau minimo 0)
            
    if janela2_cima == True and posicaojanela2 <= 90:
      posicaojanela2 =  posicaojanela2 + 1
      print (" A posicao da janela 2 atual é : ", posicaojanela2)

      #botao janela 2 cima (sobe 1 grau máximo 90)
           
    else: 
       
       if janela2_baixo == True and posicaojanela2 >= 0:
            posicaojanela2 = posicaojanela2 -1 
            print (" A posicao da janela 2 atual é : ", posicaojanela2)

            #botao janela 2 baixo (desce 1 grau minimo 0)

    if posicaojanela1 == 0 and posicaojanela2 == 0:
        posicaojanela2  = 10
        print (" NÃO É POSSIVEL COLOCAR AS 2 JANELAS TOTALMENTE FECHADAS")
        print (" A posicao da janela 1 atual é : ", posicaojanela1)
        print (" A posicao da janela 2 atual é : ", posicaojanela2)
    # coloca a janela 2 a 10º graus se as 2 tiverem totalmente fechadas

    else:
        if posicaojanela1  == 90 and posicaojanela2 == 90:
                 print (" NÃO É POSSIVEL COLOCAR AS 2 JANELAS TOTALMENTE ABERTAS")
                 print (" A posicao da janela 1 atual é : ", posicaojanela1)
                 print (" A posicao da janela 2 atual é : ", posicaojanela2)
                 Posicaojanela2  = 80

                #coloca a janela 2 a 80 graus se as 2 janelas tiverem totalmente abertas




       

 