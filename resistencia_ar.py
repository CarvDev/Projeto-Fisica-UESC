# arquivo de teste para o sistema de resistência do ar

import numpy as np
import matplotlib.pyplot as plt

m = 5.0 # massa de 5kg
g = 9.8 # aceleração da gravidade de 9,8m/s²
k = 0.0144 # constante de resistência do ar: 0,0144 (N x s²)/m² 

vt = np.sqrt((m * g) / k) # velocidade terminal
t = np.arange(0, 11, 1) #array de tempo (0 a 10 segundos)

v1 = g * t # velocidades sem resistência do ar
print("\n--- Velocidades SEM Resistência (m/s) ---")
for tempo, velocidades in zip(t, v1):
    print(f"  t={tempo} s -> v={velocidades:.2f} m/s")

v2 = vt * np.tanh((g * t) / vt) # velocidades com resistência do ar
print("\n--- Velocidades COM Resistência (m/s) ---")
for tempo, velocidades in zip(t, v2):
    print(f"  t={tempo} s -> v={velocidades:.2f} m/s")

# Planos futuros: Exportar esse código para um notepad do Jupyter, criar um novo array para 
# os valores de energia cinética ao longo do percurso, em seguida, comparar com a energia potencial e
# mostrar que houve a dissipação de energia por parte da resistência do ar através de gráficos com
# esses valores