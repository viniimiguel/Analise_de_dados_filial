import pandas as pd
from IPython.display import display


class Analise():
    def __init__(self):
        self.tabela = pd.read_excel('base_de_dados.xlsx')


    def mostrar_tabela(self):
        display(self.tabela)

    def faturamento_total(self):
        faturamento = self.tabela["Valor Total (R$)"].sum()
        faturamento_inteiro = int(faturamento)
        print(f'O FATURAMENTO TOTAL SOMANDO TODAS AS FILIAIS E DE {faturamento_inteiro} (R$)')

    def faturamento_por_loja(self):
        ft_lj = self.tabela[['Filial','Valor Total (R$)']].groupby('Filial').sum()
        display(ft_lj)

    def faturamento_por_produto(self):
        ft_pd = self.tabela[['Filial','Produto','Valor Total (R$)']].groupby(['Filial','Produto']).sum()
        display(ft_pd)




analise = Analise()
analise.mostrar_tabela()
analise.faturamento_total()
analise.faturamento_por_loja()
analise.faturamento_por_produto()
