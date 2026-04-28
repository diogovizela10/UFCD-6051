#ciclo principal
while True:
    #Dados de entrada
    dinheiro_certo = True
    botao_tirar_acucar = True
    botao_colocar_acucar = False

    config = {
    "Produtos": {
        "Cafe_Longo": {
            "Preco": 0.5,
            "tem_palheta": True,
            "tem_acucar": True,
            "tem_copo": True,
            "nivel_acucar" : 5,
            "botao_cafe_longo": "periferico_1"
        },

        "Cafe_Curto": {
            "Preco": 0.5,
            "tem_palheta": True,
            "tem_acucar": True,
            "tem_copo": True,
            "nivel_acucar" : 2,
            "botao_cafe_curto": "periferico_2"
        },

        "Cha": {
            "Preco": 0.2,
            "tem_palheta": False,
            "tem_acucar": False,
            "tem_copo": True,
            "nivel_acucar" : 2,
            "botao_cha": "periferico_3"
        },

        "Capuccino": {
            "Preco": 0.6,
            "tem_palheta": True,
            "tem_acucar": True,
            "tem_copo": True,
            "nivel_acucar" : 2,
            "botao_capuccino": "periferico_2"
        }
    }
}
    config["Produtos"]
    config["Produtos"]["Cha"]
    precodocha = config["Produtos"]["cha"]["Preco"]
    botao_cafe_longo = config["Produtos"]["cafe_longo"]["botao_cafe_longo"]
    #processamento

    if botao_cafe_longo and dinheiro_certo:
        if config["Produtos"]  ["cafe_longo"]["tem_copo"]:
            Colocar_copo = ()
        else:
            nao_colocar_copo = ()

            if (botao_tirar_acucar == True and config["produtos"]["cafe_longo"]["nivel_acucar"] >=0): #verificar se o botao esta ligado e se o nivel de acucar e maior que 0
                config["produtos"]["cafe_longo"]["nivel_acucar"]-=1

    else:
         if   (botao_colocar_acucar ==True and config["produtos"]["cafe_longo"]["nivel_acucar"] <=5): #verificar se o botao esta desligado e se o nivel de acucar e menor que o maximo
                config["produtos"]["cafe_longo"]["nivel_acucar"]+=1

                def colocar_copo():
                     """Codigo para pedir a maquina para tirar copo"""
                     print("Tirar copo")
