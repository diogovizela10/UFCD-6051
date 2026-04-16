#ciclo principal
while True:

    #Dados de entrada

    Utilizador = True
    Password = True
    Lista_Banidos = ("Rui Machado", "João Magalhães")

    #Processamento

    if Utilizador == True and Password == True and Utilizador not in Lista_Banidos: 
         print("Login efetuado com sucesso!")
         Abrir_formulario = True
    else:  
      print("Utilizador ou password incorretos!")
      Abrir_formulario = False
     
     #Dados de saída 