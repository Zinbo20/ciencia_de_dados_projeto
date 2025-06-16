import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulando os dados
np.random.seed(42)
n = 100
renda = np.random.normal(5000, 1500, n)  # renda mensal em reais
valor_medio_compra = renda * 0.15 + np.random.normal(0, 200, n)  # valor médio das compras com ruído

# Criando DataFrame
df = pd.DataFrame({
    'Renda': renda,
    'Valor_Medio_Compra': valor_medio_compra
})

# Calculando a correlação
correlacao = df.corr(method='pearson').loc['Renda', 'Valor_Medio_Compra']
print(f"Coeficiente de Correlação de Pearson: {correlacao:.2f}")

# Visualizando a relação
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='Renda', y='Valor_Medio_Compra', scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
plt.title('Correlação entre Renda e Valor Médio das Compras')
plt.xlabel('Renda Mensal (R$)')
plt.ylabel('Valor Médio das Compras (R$)')
plt.grid(True)
plt.tight_layout()
plt.show()
