while True:
  #ciclo Principal

  interruptor_A =False
  interruptor_B = True

  # processamento
  if (not interruptor_A  and interruptor_B) or (interruptor_A and not interruptor_B):

    liga_luz = True

  else:

    liga_luz = False

    if interruptor_A ^ interruptor_B:

        liga_luz = True 

    else:

        liga_luz = False    
