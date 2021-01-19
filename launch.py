#!/usr/local/bin/python3

from own_packages.send_email.send_email import send_email
from m2go import check_price as m2go
from labaie import check_price as labaie
import time
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


if __name__ == '__main__':
    while True:
        now = datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        try:
            with webdriver.Chrome(ChromeDriverManager().install()) as driver:
                m2go(driver)
                labaie(driver)
            print(f'Fin des vérifications: {date}')
            time.sleep(86400*7)
        except Exception as e:
            print('===== THERE WAS AN ERROR =====')
            send_email(['dandanny13.levy@gmail.com'], 'There was an error in: Webscrapping-Table',
                       f'There was an error: {e}')
            time.sleep(3600*2)
