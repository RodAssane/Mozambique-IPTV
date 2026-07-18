from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

URL = "https://www.tvm.co.mz/index.php/tvm-online/programacao"


def obter_programacao():

    print("A abrir TVM...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, wait_until="networkidle")
        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "lxml")

    programas = []

    for row in soup.find_all("tr"):

        hora = row.find("td", class_="time")
        titulo = row.find("td", class_="title")

        if not hora or not titulo:
            continue

        programas.append({
            "hora": hora.get_text(strip=True),
            "titulo": titulo.get_text(" ", strip=True)
        })

    return programas


if __name__ == "__main__":
    programas = obter_programacao()
    print(programas[:10])