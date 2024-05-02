import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, uniform

# Definindo os valores para o eixo x
x = np.linspace(-3, 3, 1000)

# Gerando as funções de distribuição acumulada para cada distribuição
y_normal = norm.cdf(x)
y_expon = expon.cdf(x)
y_uniform = uniform.cdf(x, loc=-3, scale=6)  # loc é o ponto inicial, scale é a largura

# Criando os gráficos
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(x, y_normal, label="Normal")
plt.title("Função de Distribuição Acumulada - Normal")
plt.ylabel("Probabilidade")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(x, y_expon, label="Exponencial", color='orange')
plt.title("Função de Distribuição Acumulada - Exponencial")
plt.ylabel("Probabilidade")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(x, y_uniform, label="Uniforme", color='green')
plt.title("Função de Distribuição Acumulada - Uniforme")
plt.ylabel("Probabilidade")
plt.xlabel("x")
plt.grid(True)

plt.tight_layout()
plt.show()
