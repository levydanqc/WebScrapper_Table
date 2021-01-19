from own_packages.send_email.send_email import send_email
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def check_price(driver):
    url = 'https://www.labaie.com/product/distinctly-home-paxton-table-à-manger-0600088144341.html?dwvar_0600088144341_color=BROWN-BLACK'

    with driver as page:
        page.minimize_window()
        page.get(url)

        price = WebDriverWait(page, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.prices > div.price > span.prod-price > span.price')))

        price = price.text.replace(' $', '').replace(
            'Price reduced from\n', '').replace('to\n', '').replace('.', '').replace(',', '.').split('\n')

        if price[0] != '1299':
            discount = round(float(price[0])-float(price[1]), 2)
            send_email(['dandanny13.levy@gmail.com', 'stephanelevy@me.com'], "Rabais chez La Baie d'Hudson",
                       f"Rabais de {discount} sur l'article:\n{url}.\nPrix de base: {price[0]} $\nPrix promotionnel: {price[1]} $")


if __name__ == "__main__":
    check_price()
