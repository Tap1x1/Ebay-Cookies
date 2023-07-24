import pickle
import pprint
import time
from webbrowser import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

name = 'main'
item_1 = input("Введите название товара №1 : ")
price_1 = input("Введите цену от ...")
price_2 = input("Введите цену до ...")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class Item:
    driver.get("https://www.ebay.com/")

    elem = driver.find_element(By.NAME, "_nkw")
    elem.send_keys(item_1)
    elem.send_keys(Keys.RETURN)
    driver.execute_script("window.scrollTo(0, 1600)")
    time.sleep(3)

    elem = driver.find_element(By.XPATH, '//*[@id="s0-53-17-0-1-2-6-1-8[3]-0-textrange-beginParamValue-textbox"]')
    elem.send_keys(price_1)

    time.sleep(1)

    elem = driver.find_element(By.XPATH, '//*[@id="s0-53-17-0-1-2-6-1-8[3]-0-textrange-endParamValue-textbox"]')
    elem.send_keys(price_2)

    time.sleep(1)
    elem.send_keys(Keys.RETURN)

    link_1 = []
    search = driver.find_elements(By.CLASS_NAME, 's-item__link')
    for ii in search:
        href = ii.get_attribute('href')
        link_1.append(href)

    driver.get(link_1[1])

    driver.execute_script("window.scrollTo(0, 1000)")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 0)")

    driver.find_element(By.ID, "mainImgHldr").click()
    time.sleep(3)

    hover = driver.find_element(By.XPATH, '//*[@id="PicturePanel"]/div/div/div[2]/div/div[2]/div[3]/div[1]/div/button[2]')
    ActionChains(driver).move_to_element(hover).perform()
    hover.click()

    time.sleep(1)

    hover = driver.find_element(By.XPATH, '//*[@id="PicturePanel"]/div/div/div[2]/div/div[2]/div[3]/div[1]/div/button[2]')
    ActionChains(driver).move_to_element(hover).perform()
    hover.click()

    time.sleep(1)

    hover = driver.find_element(By.XPATH, '//*[@id="PicturePanel"]/div/div/div[2]/div/div[2]/div[2]/button')
    ActionChains(driver).move_to_element(hover).perform()
    hover.click()

    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 200)")
    time.sleep(5)

    try:
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(driver.find_element(By.CLASS_NAME, 'fake-link').click()))
    except:
        pass

    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[3]/div[1]/div[2]/div/ul/li/div/div/div/div[2]/span[2]/button').click()


    print("deleted")
    driver.back()
    driver.back()

    i = 2
    while i < 3:
        driver.get(link_1[i])

        try:
            driver.find_element(By.ID, "mainImgHldr")
            driver.execute_script("window.scrollTo(0, 1000)")
            time.sleep(5)
            driver.execute_script("window.scrollTo(0, 50)")

            driver.find_element(By.ID, "mainImgHldr").click()
            time.sleep(3)

            hover = driver.find_element(By.XPATH, '//*[@id="PicturePanel"]/div/div/div[2]/div/div[2]/div[3]/div[1]/div/button[2]')
            ActionChains(driver).move_to_element(hover).perform()
            hover.click()

            time.sleep(3)

            hover = driver.find_element(By.XPATH, '//*[@id="PicturePanel"]/div/div/div[2]/div/div[2]/div[3]/div[1]/div/button[2]')
            ActionChains(driver).move_to_element(hover).perform()
            hover.click()

            time.sleep(1)

            driver.find_element(By.XPATH, '//*[@id="PicturePanel"]/div/div/div[2]/div/div[2]/div[2]/button').click()

            time.sleep(1)

            try:
                element = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((driver.find_element(By.XPATH, '//*[@id="mainContent"]/form/div[2]/div/div[1]/div[2]/ul/li[2]/div').click()))
                )
            except:
                pass
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[3]/div[1]/div[2]/div/ul/li/div/div/div/div[2]/span[2]').click()
            time.sleep(1)
            driver.back()
        except NoSuchElementException:
            driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[3]/div[3]/div[2]/form/div[2]/div["
                                         "1]/div[4]/span/a").click()
            pass
            time.sleep(3)
            driver.find_element(By.XPATH, "//*[@id='mainContent']/div/div[3]/div[1]/div/div/div["
                                         "2]/div/div/div/div/div[2]/span[2]").click()
            time.sleep(1)
            driver.back()
        i = i + 1

    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    pprint.pprint(driver.get_cookies())
    assert "No results found." not in driver.page_source


def main():
    webdriver.Chrome()


if name == "main":
    main()
