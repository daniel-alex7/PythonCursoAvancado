"""
CONSTANTE = "Váriáveis que não vão mudar

Muita condições no mesmo if é ruim <- Contagem de complexidade (ruim)

"""

velocidade = 65
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_pas = velocidade > RADAR_1
multado_rad1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and  local_carro <= (LOCAL_1 + RADAR_RANGE)

if vel_carro_pas:
    print("elocidade Carro passou no radar 1")

if local_carro:
     print("Carro passou no radar 1")

if multado_rad1 and vel_carro_pas:
     print("Passou do radar 1 MULTADO")