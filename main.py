#import libraries
import time
import json
import logging 

from pathlib import Path 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import scrapingDEL as sm
import scrapingOUT as so
import utils.str as str_utils 
import utils.utility as utils
from utils.logging_setup import setup_logger

# set up logging 
setup_logger(env="production")

logging.info("Reading config stuff")

# reading config file stuff 
json_config = str_utils.read_json(file_path="config.json")

# get dns name 
dns = json_config.get("dns")
# driver set up 
driver_path = json_config.get("chrome_driver_path")
driver = webdriver.Chrome(driver_path)
# files path set up
testing_files_path = json_config.get("testing_files_path")
# category set up
shift_report_category = json_config.get("shift_report_category")
# report set up
report_name = json_config.get("report")


def main(dns: str, driver, testing_files_path: str):
    """
    function to run macromBots 

    dns: the name 
    driver: chrome driver
    """
    while True:     
        try:
            #Test for mpc
            driver.get(f"{dns}/#/pages/login")
            driver = sm.logIn(driver)

            options = utils.create_menu()
            for entry in options: 
                print (entry, options[entry])

            print("Please Select:")
            selection = input() 
            if selection == '1': 
                driver.get(f"{dns}/#/event-log")
                #Test the creating event functionality
                driver = sm.createDEL(driver)

                #Test the updating event functionallity
                driver = sm.updateDEL(driver)

                #Test the attach file functionallity
                driver = sm.attachDelFiles(driver, testing_files_path)

                #Test the comments
                driver = sm.addComments(driver)

                #Test Shift Report
                driver = sm.shiftReport(driver, shift_report_category, report_name)

                time.sleep(10)

            elif selection == '2':
                print("Not available for the moment")
            elif selection == '3':
                time.sleep(2)
                driver.get(f"{dns}/#/outage-schedule")
                
                #Test the creating  outages
                time.sleep(2)
                driver = so.createOut(driver)
                #UpdateOut
                time.sleep(2)
                driver = so.updateOut(driver)

                time.sleep(2)
                driver = so.StationOut(driver)

            elif selection == '4':
                break

            else:
                print("Invalid Option")
        except Exception as e:
            logging.error("An error has occured.")
            logging.error(e)


if __name__ == "__main__":
    main(dns, driver, testing_files_path)
