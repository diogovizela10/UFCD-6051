#ciclo principal
while True: 
    #dados de entrada
    planta = 1
    cacto = 2
    sensor_humidade = 20
    tempo = 20

    if planta == cacto and sensor_humidade <= 2 and tempo >= 36:
        regar_planta = True
    else:
        regar_planta = False