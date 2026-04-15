 #ciclo Principal
while True:
 
  sensor_porta = False
  sinal_comando = False

  # processamento
  if not ((not sensor_porta  and sinal_comando) or (sensor_porta and not sinal_comando)):

    validar  = True

  else:

    validar = False

if not(sensor_porta ^ sinal_comando):

    validar = True

else:   