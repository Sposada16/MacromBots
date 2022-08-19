#import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def logIn(driver):
    #Log in to the application
    time.sleep(5)
    wait = WebDriverWait(driver, 10)
    search = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    search.send_keys("sposada")

    search = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    search.send_keys("1234@mac")
    search.send_keys(Keys.ENTER)

    time.sleep(5)

    return driver

def createDEL(driver):

    #Go to Daily Event Log module and create a new event
    try:
        waitb = WebDriverWait(driver, 20)
        # click new event
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary highlight btn-sm']"))).click()

        # click the asset dropdown
        #testing
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-select-container ng-has-value']"))).click()

        # click highlighted value
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-selected ng-option-marked ng-star-inserted']"))).click()

        #click on the region dropdown
        time.sleep(0.5)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='division']"))).click()

        #click highlighted value
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

        #click on the region dropdown
        time.sleep(0.5)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='area']"))).click()

        #click highlighted value
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

        #click on the system dropdown
        time.sleep(0.5)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='customLocationField1']"))).click()

        #click highlighted value
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

        #click on the location dropdown
        time.sleep(0.5)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='location']"))).click()

        #click highlighted value
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

        #click on the event type dropdown
        time.sleep(0.5)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='eventType']"))).click()

        #click highlighted value
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

        #submit button
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary highlight']"))).click()

        print("Event created successfully")

    except Exception as ex:
        print(ex)

    return driver

def updateDEL(driver):

    #update the created event
    try:
        waitb = WebDriverWait(driver, 20)

        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='callerContactName']"))).send_keys("Test callee")

        # click highlighted value
        time.sleep(1)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-sm btn-primary highlight event_btn_save']"))).click()

        print("Event updated successfully")
    except Exception as ex:
        print(ex)

    return driver


def attachDelFiles(driver):

    #attach files to created event
    try:
        waitb = WebDriverWait(driver, 20)

        time.sleep(10)
        #Go to files tab
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ul[@role='tablist']/li[3]"))).click()

        # upload test file
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ul[@role='tablist']/li[3]"))).click()

        print("File updated successfully")
    except Exception as ex:
        print(ex)

    return driver