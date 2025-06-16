import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulando dados de 100 clientes
np.random.seed(42)
ticket_medio = np.random.normal(loc=150, scale=30, size=100)
renda = np.random.normal(loc=5000, scale=1000, size=100)

df = pd.DataFrame({
    'Ticket_Medio': ticket_medio,
    'Renda': renda
})

# Criando visualizações

plt.figure(figsize=(15, 5))

# 1. Histograma do ticket médio
plt.subplot(1, 3, 1)
sns.histplot(df['Ticket_Medio'], bins=10, kde=True, color='skyblue')
plt.title('Distribuição do Ticket Médio')
plt.xlabel('Ticket Médio (R$)')
plt.ylabel('Frequência')

# 2. Boxplot do ticket médio
plt.subplot(1, 3, 2)
sns.boxplot(x=df['Ticket_Medio'], color='orange')
plt.title('Resumo Estatístico (Boxplot)')
plt.xlabel('Ticket Médio (R$)')

# 3. Gráfico de dispersão entre renda e ticket médio
plt.subplot(1, 3, 3)
sns.scatterplot(data=df, x='Renda', y='Ticket_Medio', color='green')
sns.regplot(data=df, x='Renda', y='Ticket_Medio', scatter=False, color='red', label='Tendência')
plt.title('Relação entre Renda e Ticket Médio')
plt.xlabel('Renda Mensal (R$)')
plt.ylabel('Ticket Médio (R$)')
plt.legend()

plt.tight_layout()
plt.show()