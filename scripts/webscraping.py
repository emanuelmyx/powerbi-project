"""
Web Scraping – Categorias de E-commerce
Fonte: books.toscrape.com (site público criado para fins educacionais de scraping)
Objetivo: Coletar nomes de produtos e preços para enriquecer a análise.
"""

import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "http://books.toscrape.com/catalogue/"
START_URL = "http://books.toscrape.com/catalogue/page-1.html"

def scrape_products(max_pages=3):
    """
    Realiza scraping de até max_pages páginas do site books.toscrape.com.
    Retorna lista de dicionários com título e preço de cada produto.
    """
    produtos = []
    url = START_URL

    for page in range(1, max_pages + 1):
        print(f"Coletando página {page}...")
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"Erro na página {page}: status {response.status_code}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        artigos = soup.find_all("article", class_="product_pod")

        for artigo in artigos:
            titulo = artigo.find("h3").find("a")["title"]
            preco_raw = artigo.find("p", class_="price_color").text.strip()
            # Remove símbolo de moeda e converte para float
            preco = float(preco_raw.replace("Â£", "").replace("£", "").strip())
            disponibilidade = artigo.find("p", class_="instock availability").text.strip()

            produtos.append({
                "titulo": titulo,
                "preco_gbp": preco,
                "disponibilidade": disponibilidade,
                "pagina": page
            })

        # Busca link da próxima página
        proxima = soup.find("li", class_="next")
        if proxima:
            url = BASE_URL + proxima.find("a")["href"]
        else:
            break

        time.sleep(1)  # Respeita o servidor

    return produtos


def salvar_csv(produtos, caminho="dados_scraping.csv"):
    """Salva a lista de produtos em CSV."""
    if not produtos:
        print("Nenhum produto para salvar.")
        return

    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=produtos[0].keys())
        writer.writeheader()
        writer.writerows(produtos)

    print(f"{len(produtos)} produtos salvos em '{caminho}'")


if __name__ == "__main__":
    print("Iniciando web scraping...")
    dados = scrape_products(max_pages=3)
    salvar_csv(dados, "dados_scraping.csv")
    print("Scraping concluído!")

    # Exibe amostra
    print("\nAmostra dos dados coletados:")
    for p in dados[:5]:
        print(f"  {p['titulo'][:50]:<50} | £{p['preco_gbp']:.2f}")
