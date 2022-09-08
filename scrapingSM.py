#import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time

def createShift(driver):
    try:
        waitb = WebDriverWait(driver, 20)
        # click new shift
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary highlight btn-sm']"))).click()

        #click previous controller dropdown
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@class='ng-select-searchable ng-select-clearable ng-select ng-select-single ng-untouched ng-pristine ng-invalid']//div[@class='ng-select-container']"))).click()

        #select previous controller
        time.sleep(0.5)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

        #click submit button
        time.sleep(0.5)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))).click()

        print("Shift created successfully")

    except Exception as ex:
        print(ex)

    return driver

def checkinForm(driver):
    try:
        waitb = WebDriverWait(driver, 20)

        # Click on the checkin form tab
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ul[@role='tablist']/li[4]"))).click()

        # write description
        time.sleep(2)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@class='form-control t-text-area ng-untouched ng-pristine ng-invalid']"))).send_keys("Testing in process.....")

        # sign off
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign-Off']"))).click()
        time.sleep(2)
        Alert(driver).accept()
        time.sleep(3)

        print("Check In Form Signed")

    except Exception as ex:
        print(ex)

    return driver

def checkoutForm(driver):
    try:
        waitb = WebDriverWait(driver, 20)

        # Click on the checkout form tab
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ul[@role='tablist']/li[5]"))).click()

        # write description
        time.sleep(2)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@class='form-control t-text-area ng-untouched ng-pristine ng-invalid']"))).send_keys("Testing in process.....")

        # sign off
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign-Off']"))).click()
        time.sleep(2)
        Alert(driver).accept()
        time.sleep(3)

        print("Check Out Form Signed")

    except Exception as ex:
        print(ex)

    return driver

def shiftHandover(driver):
    try:
        waitb = WebDriverWait(driver, 20)

        # Click on the handover tab
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ul[@role='tablist']/li[7]"))).click()

        # Click initiate shift handover
        time.sleep(2)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Initiate Shift Handover']"))).click()

        time.sleep(2)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button-collapse ng-star-inserted']"))).click()

        # click checkout button
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #ActionChains(driver).scroll_from_origin(scroll_origin, 0, 200).perform()
        time.sleep(4)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Checkout']"))).click()

        # click next controller dropdown
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@class='ng-select-searchable ng-select ng-select-single ng-untouched ng-pristine ng-invalid']//div[@class='ng-select-container']"))).click()

        #select next controller
        time.sleep(0.5)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

        # click submit button
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))).click()


        print("Check Out Form Signed")

    except Exception as ex:
        print(ex)

    return driver