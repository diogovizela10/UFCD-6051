#ciclo principal
while True:

    #Dados de entrada

    sensor_de_temperatura = 30

    #Processamento

    if sensor_de_temperatura >= 40:

        print("Temperatura elevada, ligar o ar condicionado")
        ativa_arcondicionado = True

    else:    
         
         ativa_arcondicionado = False

     #Dados de saída 