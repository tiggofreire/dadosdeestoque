import matplotlib.pyplot as plt

produtos = ['Teclado','Mouse','Monitor','Webcam']
quantidades = [50, 75, 30, 60]
cores = ['green', 'gray' ,'black' ,'purple']
categorias=['Teclado' ,'Mouse' ,'Monitor' ,'Webcam']

plt.bar(produtos, quantidades, color=cores, label=categorias)

plt.title("Estoque Atual por Categoria de Produto")
plt.legend()
plt.xlabel("Categorias")
plt.ylabel("Quantidade")
plt.show()
