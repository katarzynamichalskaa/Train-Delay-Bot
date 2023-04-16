from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


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
    start_station.send_keys("KRAKÓW GŁÓWNY")

    #DESTINATION STATION
    destination_station = driver.find_element(By.ID, 'to-station')
    destination_station.send_keys("GDAŃSK GŁÓWNY")

    #SEARCH BUTTON
    search_button = driver.find_element(By.ID,'singlebutton')
    search_button.click()

    #DELAY CHECKING
    time.sleep(3)

    on_schedule_train = driver.find_elements(By.CLASS_NAME, 'clear-lowres')
    delayed_train = driver.find_elements(By.CLASS_NAME, 'prognosis')

    delayed_train_list = []
    on_schedule_train_list = []

    for i, train in enumerate(delayed_train):
        delayed_train_list.append('0')
        if train.find_elements(By.CSS_SELECTOR, "span[class='rtinfo']"):
            print(f"Train with delay found at index {i}")
            delayed_train_list.append(train.text)

    for train in on_schedule_train:
        if train.find_elements(By.CSS_SELECTOR, "span[class='wcag-hide']"):
            on_schedule_train_list.append(train.text.strip().replace('\n', '').strip().replace('PRZYJAZD', '').strip().replace('ODJAZD', ''))

    result_delayed = []
    result_on_schedule_train_list = []

    for i in range(0, len(delayed_train_list)-1, 2):
        result_delayed.append((delayed_train_list[i], delayed_train_list[i+1]))
        result_on_schedule_train_list.append((on_schedule_train_list[i], on_schedule_train_list[i + 1]))

    last_list = list(zip(result_delayed, result_on_schedule_train_list))
    print(last_list)
    driver.quit()

    return last_list

