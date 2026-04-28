#ciclo Principal 
while True: 
    #Dados de entrada 

    config_maquina1 = {
    "Referencia": "Primec",
    "Tipo": "Gravadora",
    "Velocidade": 8,
    "Temperatura": 200,
    "Consumo": "3000 W",
    "Presso": 6,
    "Modo": "Automático",
    "Ligada": True
}

    config_maquina2 = {
    "Referencia": "Impianti",
    "Tipo": "Máquina de Revestimento",
    "Velocidade": 20,
    "Temperatura": 300,
    "Consumo": "10000 W",
    "Pressao": 10,
    "Modo": "Automático",
    "Ligada": False
    
}
    
    config_maquina1["velocidade"]
    botao_ligar_Primec = config_maquina1["Primec"]["ligada"]
    botao_ligar_Impianti = config_maquina1["Impianti"]["ligada"]

    
    if botao_ligar_Primec and config_maquina1["Temperatura" <= 200 and config_maquina1[" Pressao" > 2 and "Pressao" < 10 ]]:
        print("Maquina pronta para Produção")
    else:
        print("Maquina com muita temperatura ou pressão do ar não conforme")

    if botao_ligar_Impianti and config_maquina2["Temperatura" <= 500 and config_maquina2[" Pressao" > 6 and "Pressao" < 20 ]]:
        print("Maquina pronta para Produção")
    else:
        print("Maquina com muita temperatura ou pressão do ar não conforme")
       

