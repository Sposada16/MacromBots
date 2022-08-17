#import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import scrapingMacrom


def main():
    driver = scrapingMacrom.setChromeDriver()

    #Test for mpc
    driver.get("https://mpc-dev.macrom.online/#/pages/login")
    driver = scrapingMacrom.logIn(driver)

    driver.get("https://mpc-dev.macrom.online/#/event-log")
    #Test the creating event functionality
    driver = scrapingMacrom.createDEL(driver)

    #Test the updating event functionallity
    driver = scrapingMacrom.updateDEL(driver)

    time.sleep(10)


if __name__ == "__main__":
    main()
