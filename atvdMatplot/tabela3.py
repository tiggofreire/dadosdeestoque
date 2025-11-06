import matplotlib.pyplot as plt

categorias = ['Eletrônicos', 'Vestuário', 'Alimentos']
valores = [15000, 8000, 5000]
cores = ["gray", "green", "yellow"]

plt.pie(valores, labels=categorias, colors=cores)
plt.title("Mix de Estoque Baseado no Valor Geral")
plt.show()