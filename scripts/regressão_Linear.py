import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Simulando dados
np.random.seed(42)
investimento = np.random.uniform(10, 100, 50)  # investimento em marketing (mil R$)
vendas = 2.5 * investimento + np.random.normal(0, 10, 50)  # vendas com alguma variação aleatória

# Colocando em um DataFrame
df = pd.DataFrame({
    'Investimento': investimento,
    'Vendas': vendas
})

# Preparando os dados para regressão
X = df[['Investimento']]  # variável independente (precisa ser 2D para o scikit-learn)
y = df['Vendas']          # variável dependente

# Criando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X, y)

# Coeficientes
coeficiente = modelo.coef_[0]
intercepto = modelo.intercept_

print(f"Equação da reta: Vendas = {coeficiente:.2f} * Investimento + {intercepto:.2f}")

# Fazendo previsões
df['Vendas_Previstas'] = modelo.predict(X)

# Visualizando os dados e o modelo
plt.figure(figsize=(10, 6))
plt.scatter(df['Investimento'], df['Vendas'], color='blue', label='Dados Reais')
plt.plot(df['Investimento'], df['Vendas_Previstas'], color='red', label='Regressão Linear')
plt.xlabel('Investimento em Marketing (mil R$)')
plt.ylabel('Vendas (mil unidades)')
plt.title('Regressão Linear Simples: Investimento vs Vendas')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()