import numpy as np
import pandas as pd

# Simulando dados de 30 dias
np.random.seed(42)
dias = pd.date_range(start='2024-05-01', periods=30)
vendas_diarias = np.random.randint(50, 200, size=30)  # número de vendas por dia
ticket_medio = np.random.normal(loc=150, scale=30, size=30)  # ticket médio em R$

# Criando DataFrame
df = pd.DataFrame({
    'Data': dias,
    'Vendas_Diarias': vendas_diarias,
    'Ticket_Medio': ticket_medio
})
df.set_index('Data', inplace=True)

# Calculando medidas de tendência central
media_vendas = df['Vendas_Diarias'].mean()
mediana_ticket = df['Ticket_Medio'].median()
moda_vendas = df['Vendas_Diarias'].mode().iloc[0]  # pode haver mais de uma moda

# Exibindo os resultados
print(f"Média de vendas diárias: {media_vendas:.2f}")
print(f"Mediana do ticket médio: R$ {mediana_ticket:.2f}")
print(f"Moda das vendas diárias: {moda_vendas}")

# Visualização (opcional)
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
df['Vendas_Diarias'].plot(kind='hist', bins=10, color='skyblue', edgecolor='black')
plt.axvline(media_vendas, color='red', linestyle='--', label='Média')
plt.axvline(moda_vendas, color='green', linestyle='--', label='Moda')
plt.title('Distribuição das Vendas Diárias')
plt.xlabel('Número de Vendas')
plt.legend()

plt.subplot(1, 2, 2)
df['Ticket_Medio'].plot(kind='box', vert=False, color='orange')
plt.title('Distribuição do Ticket Médio')

plt.tight_layout()
plt.show()
