import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulando dados diários para 1 ano
dias = pd.date_range(start='2022-01-01', periods=365)

# Criando uma sazonalidade com pico no inverno (junho, julho, agosto)
# Offset para deslocar o pico para o meio do ano (~dia 180)
sazonalidade = 10 + 5 * np.sin(2 * np.pi * (dias.dayofyear - 180) / 365)

# Adicionando um pouco de ruído para simular variações reais
np.random.seed(42)
ruido = np.random.normal(0, 1, size=365)

# Série final: consumo de remédios com sazonalidade + ruído
consumo = sazonalidade + ruido

# Criando DataFrame para visualização
df = pd.DataFrame({'Data': dias, 'Consumo': consumo})
df.set_index('Data', inplace=True)

# Plotando o gráfico
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Consumo'], label='Consumo de remédio (simulado)')
plt.title('Série Temporal - Consumo de Remédio para Gripe com Sazonalidade de Inverno')
plt.xlabel('Data')
plt.ylabel('Consumo')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()