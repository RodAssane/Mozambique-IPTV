from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

URL = "https://www.tvm.co.mz/index.php/tvm-online/programacao-tvm-internacional"


def obter_programacao():

    print("A abrir TVM Internacional...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, wait_until="networkidle")
        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "lxml")

    programas = []

    for row in soup.find_all("tr"):

        texto = row.get_text(" ", strip=True)

        if not texto:
            continue

        partes = texto.split(" ", 1)

        if len(partes) != 2:
            continue

        hora = partes[0]
        titulo = partes[1]

        if ":" not in hora:
            continue

        programas.append({
            "hora": hora,
            "titulo": titulo
        })

    return programas


if __name__ == "__main__":
    programas = obter_programacao()
    print(programas[:10])