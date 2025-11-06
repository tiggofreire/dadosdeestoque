import matplotlib.pyplot as plt

dias = [1, 2, 3, 4, 5, 6, 7]
estoque = [100, 95, 110, 105, 120, 115, 130]

plt.plot(dias, estoque, color="blue",label="Estoque")
plt.xlabel("DIAS")
plt.ylabel("ESTOQUE")
plt.title("Fluxo de Estoque Semanal")
plt.grid(True)
plt.legend()
plt.show()