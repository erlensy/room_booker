from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os, time, getpass

def bookRoom(username, password, startTime, endTime, date, bookingText, roomId, headless = False):
    chromeOptions = webdriver.ChromeOptions()

    if headless == True:
        chromeOptions.headless = True

    chromedriverPath = Service(os.path.abspath(os.getcwd()) + "/chromedriver")
    browser = webdriver.Chrome(service=chromedriverPath, chrome_options=chromeOptions)

    startUrl = "https://tp.uio.no/ntnu/rombestilling/"
    browser.get(startUrl)

    element = browser.switch_to.active_element
    element.send_keys("NTNU")
    for _ in range(2):
        element.send_keys(Keys.RETURN)
        element = browser.switch_to.active_element
    element.send_keys(Keys.RETURN)

    element = browser.find_element(By.NAME, "feidename")
    element.send_keys(username)

    element = browser.find_element(By.NAME, "password")
    element.send_keys(password)
    element.send_keys(Keys.RETURN)

    specificRoomUrl = "https://tp.uio.no/ntnu/rombestilling/?start=" + startTime + "&preset_date=" + date + "&roomid=" + roomId
    browser.get(specificRoomUrl)

    element = browser.switch_to.active_element
    for _ in range(25):
        element.send_keys(Keys.TAB)
    element = browser.switch_to.active_element
    element.send_keys(Keys.RETURN)
    element = browser.switch_to.active_element
    element.send_keys(endTime)
    element.send_keys(Keys.RETURN)

    element = browser.find_element(By.NAME, "preformsubmit")
    element.click()

    element = browser.find_element(By.ID, "rb-bestill")
    element = browser.switch_to.active_element
    element.send_keys(Keys.RETURN)

    element = browser.switch_to.active_element
    element.send_keys(bookingText)
    element.send_keys(Keys.RETURN)
