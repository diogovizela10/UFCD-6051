#ciclo principal

while True:

    # dados de entrada

    quadro = {
        "corte_geral": {
            "In_corrente": 32,
            "Tensao": 400,
            "tipo": "Disjuntores",
            "Disjuntores": [
                {
                    "nome": "Diferencial",
                    "delta1": 0.03,
                    "In": 32,
                    "referencia": "Schneider Electric A9Z01440 IDK",
                    "modelo": "Interruptor trifásico 3P+N",
                    "tensao": "400V",
                    "corrente_nominal": "40A",
                    "fabricante": "Schneider Electric"
                },
                {
                    "nome": "Disjuntor Luz",
                    "referencia": "Schneider Electric R9P35616-1P+N",
                    "In": 10,
                    "modelo": "Disjuntor magnetotérmico",
                    "tensao": "230V/400V",
                    "poder_corte": 4.5,
                    "fabricante": "Schneider Electric"
                },
                {
                    "nome": "Disjuntor Tomadas",
                    "referencia": "Schneider Electric R9P35620-1P+N",
                    "In": 16,
                    "modelo": "Disjuntor magnetotérmico",
                    "tensao": "230V",
                    "corrente_nominal": "20A",
                    "poder_corte": 4.5,
                    "fabricante": "Schneider Electric"
                }
            ]
        }
    }
 
    def corte_disjuntor(quadro):

        desligar_disjuntor = False

        disjuntores = quadro["corte_geral"]["Disjuntores"]


        if disjuntores[1]["poder_corte"] >= 4.5:
            print("Carga demasiado alta")
            desligar_disjuntor = True

        elif disjuntores[2]["poder_corte"] >= 4.5:
            print("Carga demasiado alta")
            desligar_disjuntor = True

        return desligar_disjuntor
    

    lampadas = {
        "potencia" : 40,
        "tensao" : 230,
        "quantidade" : 3 }
    


    import minhas_funcoes


    corrente_de_cada_lampada = lampadas["potencia"]/lampadas["tensao"]
    corrente_de_todas_lampadas = corrente_de_cada_lampada * lampadas["quantidade"]
    corrente_de_todas_lampadas

    minhas_funcoes.selecionar_dinjuntor(corrente_de_todas_lampadas)

    print("Corrente de cada lampada", corrente_de_cada_lampada)
    print("Corrente de todas as lampadas", corrente_de_todas_lampadas)

