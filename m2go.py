from own_packages.send_email.send_email import send_email


def check_price(driver):
    url = 'https://www.m2go.ca/fc/table-a-manger-36x72-brun-et-noir-collection-paxto.html'

    with driver as page:
        page.get(url)
        page.minimize_window()

        price = page.find_element_by_css_selector(
            'div.row.product-price > div > div.price-wrap > p.prices')

        price = price.text.replace(' $', '').split(' ')

        if price[0] != '649':
            discount = round(float(price[1])-float(price[0]), 2)
            send_email(['dandanny13.levy@gmail.com', 'stephanelevy@me.com'], 'Rabais chez M2GO',
                       f"Rabais de {discount} sur l'article:\n{url}.\nPrix de base: {price[1]} $\nPrix promotionnel: {price[0]} $")


if __name__ == "__main__":
    check_price()
