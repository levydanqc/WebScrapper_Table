from m2go import check_price as m2go
from labaie import check_price as labaie
import time
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


if __name__ == '__main__':
    while True:
        now = datetime.now().timetuple()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install())
            m2go(driver)
            labaie(driver)
            print(f'Fin des vérifications: {date}')
            time.sleep(86400*7)
        except:
            print('===== THERE WAS AN ERROR =====')
            time.sleep(3600*2)
