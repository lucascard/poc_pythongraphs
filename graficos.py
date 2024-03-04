import matplotlib.pyplot as plt

# df = pd.read_excel('fixture\excel.xlsx')

# Dados fictícios (substitua isso pelos dados do seu banco de dados)
quantidade_promotores = [1000, 1200, 1500, 1300]  # Quantidade total de promotores de venda
quantidade_vendas_total = [5000, 5500, 6000, 5800]  # Quantidade total de vendas
quantidade_vendas_app_vendedor = [2000, 2200, 2400, 2300]  # Quantidade de vendas pelo app do vendedor

# Gráfico: Quantidade total de promotores de venda ao longo dos períodos
plt.figure(figsize=(10, 5))
plt.plot(['06/02 a 12/02', '13/02 a 19/02', '20/02 a 26/02', '27/02 a 04/03'], quantidade_promotores, marker='o')
plt.title('Quantidade total de promotores de venda')
plt.xlabel('Ano')
plt.ylabel('Quantidade')
plt.grid(True)
plt.show()

# Gráfico: Quantidade de vendas nacional ao longo dos anos
plt.figure(figsize=(10, 5))
plt.plot(['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4'], quantidade_vendas_total, marker='o')
plt.title('Quantidade de vendas nacional')
plt.xlabel('Ano')
plt.ylabel('Quantidade')
plt.grid(True)
plt.show()

# Gráfico: Quantidade de vendas pelo App do vendedor ao longo dos anos
plt.figure(figsize=(10, 5))
plt.plot(['Ano 1', 'Ano 2', 'Ano 3', 'Ano 4'], quantidade_vendas_app_vendedor, marker='o')
plt.title('Quantidade de vendas pelo App do vendedor')
plt.xlabel('Ano')
plt.ylabel('Quantidade')
plt.grid(True)
plt.show()
