import time
from selenium import webdriver
import send_msg
import requests
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class Websites_checker:

    def __init__(self):
            
        self.timeout = 5
        chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

        chrome_options = Options()
        options = [
            "--headless",
            "--disable-gpu",
            "--window-size=1920,1200",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
        for option in options:
            chrome_options.add_argument(option)

        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def land_firstPage(self,domain):
        self.domain = domain
        self.driver.get(f"https://{self.domain}")

    def check_city(self):
        city_url = self.driver.find_element(By.CSS_SELECTOR,'#popular-searches li a').get_attribute('href')
        city_page = requests.get(city_url)
        if city_page.status_code == 200:
            send_msg.notify_slack(f'{city_url} | status code={city_page.status_code}' )
        print(f'{city_url} | status code={city_page.status_code}')

websites = Websites_checker()

with open('domains.txt') as file:
    domains=file.readlines()

for domain in domains:
    websites.land_firstPage(domain.strip())   
    websites.check_city()

    time.sleep(2)