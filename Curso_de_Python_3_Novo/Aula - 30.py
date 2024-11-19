""" 
Constate = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    ← Contagem de Complexidade (ruim)
"""

velocidade = 61
local = 90

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel = velocidade > RADAR_1
multa1 = local >= (LOCAL_1 + RADAR_RANGE) and \
local <= (LOCAL_1+RADAR_RANGE)
multa1 = multa1 and vel
if vel:
    print('Velocidade do carro passou do radar 1')

if multa1 and vel:
        print('Carro multado em radar 1')

