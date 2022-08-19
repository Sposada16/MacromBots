#Selenium test
#install chrome driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://mpc-dev.macrom.online/#/pages/login")

# Enter to the apppppp

wait = WebDriverWait(driver, 10)
search = wait.until(EC.presence_of_element_located((By.NAME, "username")))
search.send_keys("sposada")

search = wait.until(EC.presence_of_element_located((By.NAME, "password")))
search.send_keys("1234@mac")
search.send_keys(Keys.ENTER)


try:

    driver.get("https://mpc-dev.macrom.online/#/event-log")
    waitb = WebDriverWait(driver, 20)
    # click new event
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary highlight btn-sm']"))).click()

    # click the asset dropdown
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-select-container ng-has-value']"))).click()

    # click highlighted value
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-selected ng-option-marked ng-star-inserted']"))).click()

    #click on the region dropdown
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='division']"))).click()

    #click highlighted value
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

    #click on the region dropdown
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='area']"))).click()

    #click highlighted value
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

    #click on the system dropdown
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='customLocationField1']"))).click()

    #click highlighted value
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

    #click on the location dropdown
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='location']"))).click()

    #click highlighted value
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

    #click on the event type dropdown
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='eventType']"))).click()

    #click highlighted value
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ng-option ng-option-marked ng-star-inserted']"))).click()

    #submit button
    waitb.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary highlight']"))).click()

    print("Event created successfully")

except Exception as ex:
    print(ex)




#searchButton = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn btn-primary highlight btn-sm")))
#searchButton.click()
#driver.close() #closes tab
# driver.quit #closes browser

#HTML hierarchy, first class, then name, then worst scenarios class name but not recommended


#def main():
#if __name__ == "__main__":
    #main()