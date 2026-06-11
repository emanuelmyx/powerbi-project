# 📊 Dashboard de Vendas Virtuais— Power BI

> Trabalho Final — Disciplina: Tratamento e Análise de Dados  
> Faculdade Princesa do Oeste (FPO) — Curso de ADS

---

## 👤 Integrantes

| Emanuel Carvalho | 091.024.673-48 |
---

## 🎯 Descrição do Tema e Objetivo

**Tema:** Análise de Vendas Comercial
**Objetivo:** Desenvolver um dashboard analítico que permita identificar padrões de compra em uma plataforma de e-commerce fictícia, respondendo às seguintes perguntas de negócio:

- Quais categorias geram maior receita?
- Em quais estados/regiões as vendas são mais fortes?
- Qual canal de venda (Site, App, Marketplace) performa melhor?
- Como as vendas evoluíram ao longo do tempo?
- Qual o percentual de pedidos entregues com sucesso?

---

## 🗂️ Fontes de Dados

| Dataset Sintético | CSV gerado com Python | 1.500 pedidos simulados com dados de produtos, estados brasileiros e canais de venda | Gerado via script |
| Books to Scrape | Web Scraping | Site educacional público usado para demonstrar a técnica de scraping | http://books.toscrape.com |

---

## 🔧 Como Abrir o Arquivo

1. Certifique-se de ter o **Power BI Desktop** instalado (versão gratuita disponível em powerbi.microsoft.com)
2. Clone ou baixe este repositório
3. Abra o arquivo `dashboard/projeto_final.pbix` no Power BI Desktop
4. Os dados já estão incorporados — nenhuma conexão externa necessária

---

## 🧱 Modelagem — Esquema Estrela

O modelo segue o padrão **Star Schema** com:

- **Fac_Pedidos** — Tabela fato com todas as transações
- **Dim_Produto** — Dimensão com nome e categoria do produto
- **Dim_Localidade** — Dimensão com UF, estado e região
- **Dim_Calendario** — Dimensão de tempo (Data, Ano, Mês, Trimestre, Dia da Semana)
- **_Medidas** — Tabela auxiliar com todas as medidas DAX

---

## 📐 Medidas DAX Criadas

| Medida | Descrição |
|--------|-----------|
| Total Vendas | Soma total do valor dos pedidos |
| Média por Pedido | Ticket médio por transação |
| % Pedidos Entregues | Taxa de entrega com sucesso |
| Vendas App Mobile | Vendas filtradas pelo canal App |
| Vendas Ano Anterior | Comparação com SAMEPERIODLASTYEAR |
| Total de Pedidos | Contagem de pedidos |
| Crescimento YoY % | Variação percentual ano a ano |
| Receita Líquida | Vendas descontando o frete |

---

## 📸 Prints do Dashboard

**Página 1 — Visão Geral**
<img width="1057" height="601" alt="image" src="https://github.com/user-attachments/assets/66143a5a-1691-4736-af5f-b0f5eb0c9ead" />

**Página 2 — Análise Geográfica**
<img width="1178" height="656" alt="image" src="https://github.com/user-attachments/assets/213dfc8a-be43-4864-a68d-fec5a9e75295" />


**Página 3 — Análise Detalhada**


---

## 💡 Principais Insights Encontrados

1. **Eletrônicos** representam mais de 40% da receita total, sendo a categoria mais lucrativa
2. **São Paulo e Rio de Janeiro** concentram cerca de 35% de todos os pedidos, evidenciando desigualdade regional
3. O **App Mobile** apresenta crescimento consistente no segundo semestre, superando o Site em volume de pedidos em alguns meses
4. A taxa de entrega bem-sucedida é de aproximadamente **60%**, indicando oportunidade de melhoria na logística
5. O **ticket médio** varia significativamente por canal: Marketplace tem os maiores valores por pedido

---

## 🛠️ Tecnologias Utilizadas

- Python 3 (geração e tratamento de dados)
- BeautifulSoup (web scraping)
- Power BI Desktop (modelagem, DAX e dashboard)
- GitHub (versionamento e entrega)
