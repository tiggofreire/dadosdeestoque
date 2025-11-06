import matplotlib.pyplot as plt

precos = [50, 120, 300, 80, 20]
estoque = [80, 25, 10, 70, 150]

plt.scatter(precos, estoque, label="Produtos", color="green")
plt.legend()
plt.title("Relação entre Preço e Estoque")
plt.xlabel("Preço do Produto (R$)")
plt.ylabel("Quantidade em Estoque")
plt.grid(True)
plt.show()