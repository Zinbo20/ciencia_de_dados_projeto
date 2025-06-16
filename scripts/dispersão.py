import numpy as np
import pandas as pd

# Simulando dados de ticket médio de 100 clientes
np.random.seed(42)
ticket_medio = np.random.normal(loc=150, scale=40, size=100)  # média = 150, desvio = 40

# Colocando em DataFrame
df = pd.DataFrame({'Ticket_Medio': ticket_medio})

# Medidas de dispersão
desvio_padrao = df['Ticket_Medio'].std()
variancia = df['Ticket_Medio'].var()
amplitude = df['Ticket_Medio'].max() - df['Ticket_Medio'].min()
media = df['Ticket_Medio'].mean()
coef_var = (desvio_padrao / media) * 100  # em %

# Exibindo os resultados
print(f"Média do ticket médio: R$ {media:.2f}")
print(f"Desvio padrão: R$ {desvio_padrao:.2f}")
print(f"Variância: R$ {variancia:.2f}")
print(f"Amplitude: R$ {amplitude:.2f}")
print(f"Coeficiente de variação: {coef_var:.2f}%")

# Visualização opcional
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.hist(df['Ticket_Medio'], bins=15, color='skyblue', edgecolor='black')
plt.axvline(media, color='red', linestyle='--', label='Média')
plt.title('Distribuição do Ticket Médio')
plt.xlabel('Valor do Ticket Médio (R$)')
plt.ylabel('Número de Clientes')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()