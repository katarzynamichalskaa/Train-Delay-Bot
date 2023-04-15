from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def TrainDelays():

    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)

    driver.get("https://rozklad-pkp.pl/")
    driver.maximize_window()


    #COOKIE BUTTON
    cookie_button = driver.find_element(By.CLASS_NAME, 'css-47sehv')
    cookie_button.click()

    #INPUT STATION
    start_station = driver.find_element(By.ID, 'from-station')
    start_station.send_keys("POZNAŃ GŁÓWNY")

    #DESTINATION STATION
    destination_station = driver.find_element(By.ID, 'to-station')
    destination_station.send_keys("WRONKI")

    #SEARCH BUTTON
    search_button = driver.find_element(By.ID,'singlebutton')
    search_button.click()

    #DELAY CHECKING

    delayed_train = driver.find_elements(By.CLASS_NAME, 'prognosis')

    delayed_train_list = []

    for train in delayed_train:
        if train.find_elements(By.TAG_NAME, "img"):
            delayed_train_list.append(train.text)

    driver.quit()

    empty_list_check = 0

    if not delayed_train_list:
         print('There are no delays')
         empty_list_check = 1

    else:
         print('There are some delays:', delayed_train_list)

    return empty_list_check
