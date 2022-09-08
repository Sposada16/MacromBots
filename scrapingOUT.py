#import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def createOut (driver):
    try:
        waitb = WebDriverWait(driver, 20)
        # click new outage
        time.sleep(2)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-sm btn-primary highlight']"))).click()
        
        # Test Title
        #testing
        time.sleep(2)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='form-control ng-untouched ng-pristine ng-invalid']"))).send_keys("Test outages")

        # Desplegar-Region
        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='division']"))).click()
        
        # Seleccionar region
        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()
        
        # Desplegar area
        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='area']"))).click()

        #Seleccionar area
        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()
        
        #Añadir estacion-Boton
        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Station']"))).click()
        
        #Desplegar location
        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='c-btn']"))).click()
        
        #Select location
        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='pure-checkbox ng-star-inserted']"))).click()
        
        #Apply location
        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Apply']"))).click()

        #Despliegue WT
        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ng-select-container'])[2]"))).click()

        #Select option
        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

        #Send
        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))).click()
        
        print("Outages created successfully")
        time.sleep(3)
    except Exception as ex:
        print(ex)
    return driver

def updateOut (driver):
    try: 
        waitb = WebDriverWait(driver, 20)

        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@formcontrolname='summary']"))).send_keys("Test outages_2")

        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnSubmit']"))).click()
        
        print("Outages updated successfully")
        time.sleep(2)
    except Exception as ex:
        print(ex)
    return driver

def StationOut (driver):
    try:
        waitb = WebDriverWait(driver, 20)
        
        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//aside[@class='aside-menu']//li[4]//a[1]//*[name()='svg']"))).click()

        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='Location']//div[@class='ng-select-container']"))).click()
        
        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

        time.sleep(3)
        waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Station']"))).click()

        print("Outages Add_station successfully")
    except Exception as ex:
        print(ex)
    return driver