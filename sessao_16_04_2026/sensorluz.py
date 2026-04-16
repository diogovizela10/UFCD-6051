#ciclo principal
while True:

    #Dados de entrada

    sensor1 = 50
    sensor2 = 50
    sensor3 = 50    
    sensor4 = 50

    #Processamento

    if (sensor1 < 20 or sensor2 < 20 or sensor3 < 20 or sensor4 < 20):
      print("Pouca quantidade de luz, ligar as luzes!")
      ligar_Luzes = True 
      
    else:
        print("Quantidade de luz suficiente, desligar as luzes!")
        ligar_Luzes = False
     
     #Dados de saída 