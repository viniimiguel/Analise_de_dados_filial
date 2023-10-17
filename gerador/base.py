import pandas as pd
import random


filiais = ["Filial A", "Filial B", "Filial C", "Filial D", "Filial E"]
produtos = ["Geladeira", "Máquina de Lavar", "Micro-ondas", "Liquidificador", "Aspirador de Pó"]


data = []
for _ in range(60):  
    entrada = {
        "Filial": random.choice(filiais),
        "Produto": random.choice(produtos),
        "Quantidade Vendida": random.randint(1, 10),
        "Valor Unitário (R$)": round(random.uniform(100, 2000), 2),
    }
    entrada["Valor Total (R$)"] = entrada["Quantidade Vendida"] * entrada["Valor Unitário (R$)"]
    data.append(entrada)


df = pd.DataFrame(data)

df.to_excel("base_de_dados.xlsx", index=False)
