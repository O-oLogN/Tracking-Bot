from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException

from datetime import datetime

import time

import os

web_path = "https://www.facebook.com"

infoFile = open("C:\\Users\\hiepg\\Info.txt", "r")

info = infoFile.read().split()

user_name = info[0]

pass_word = info[1]

options = Options()

options.add_experimental_option("detach", True)

options.add_argument("--disable-notifications")

options.add_argument("--enable-javascript")

options.add_argument("--user-agent=Chrome/90.0.4430.212")

options.add_argument("--disable-features=RendererCodeIntegrity")

options.add_argument("--headless")

driver = webdriver.Chrome(options)

driver.maximize_window()

driver.get(web_path)

WebDriverWait(driver, 7200).until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")))

driver.find_element(By.NAME, "email").send_keys(user_name, Keys.ESCAPE)

driver.find_element(By.NAME, "pass").send_keys(pass_word, Keys.ENTER)

WebDriverWait(driver, 7200).until(EC.presence_of_all_elements_located(
    (By.CLASS_NAME, "xe3v8dz")))        # wait for the presence of main page

driver.get(info[2])

WebDriverWait(driver, 7200).until(EC.presence_of_all_elements_located(
    (By.CLASS_NAME, "x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.xl56j7k.x6s0dn4.xozqiw3.x1q0g3np.xi112ho.x17zwfj4.x585lrc.x1403ito.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xn6708d.x1ye3gou.xtvsq51.x1r1pt67")))        # wait for the presence of "Nhắn tin" button

driver.find_element(By.CLASS_NAME, "x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.xl56j7k.x6s0dn4.xozqiw3.x1q0g3np.xi112ho.x17zwfj4.x585lrc.x1403ito.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xn6708d.x1ye3gou.xtvsq51.x1r1pt67").click()

WebDriverWait(driver, 7200).until(EC.presence_of_all_elements_located(
    (By.CLASS_NAME, "x5yr21d.x1uvtmcs")))   # wait for the presence of message window

currentSessionDayMonthYear = ""

nameDayInTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

sessionInDay = ["night", "morning", "afternoon", "evening"]     # 0-6, 6-12, 12-18, 18-24

def GetSaveFileName():
    global currentSessionDayMonthYear
    now = datetime.now()
    currentTime = now.strftime("%H:%M")
    currentDayInWeek = now.weekday()
    currentDayInMonth = now.day
    currentMonth = now.month
    currentYear = now.year
    strFileName = f"{nameDayInTheWeek[currentDayInWeek]}-{sessionInDay[int((int(currentTime[:2]) * 60 + int(currentTime[3:5])) / 360)]}({currentDayInMonth}-{currentMonth})"
    currentSessionDayMonthYear = f"{sessionInDay[int((int(currentTime[:2]) * 60 + int(currentTime[3:5])) / 360)]}-{nameDayInTheWeek[currentDayInWeek]}-{currentDayInMonth}-{currentMonth}-{currentYear}"
    return strFileName

while True:
    tracking = open("D:\\Code\\Python\\tracking.txt", "r")

    flagOfTrackingFile = tracking.readline().strip()

    saveFileName = GetSaveFileName()

    if currentSessionDayMonthYear != flagOfTrackingFile:
        tracking_file = open("D:\\Code\\Python\\tracking.txt", "w")
        tracking_file.truncate()
        tracking_file.close()

    tracking.close()

    now = datetime.now()

    currentTime = now.strftime("%H:%M")

    tracking = open("D:\\Code\\Python\\tracking.txt", "a")

    if os.stat("D:\\Code\\Python\\tracking.txt").st_size == 0:
        tracking.write(currentSessionDayMonthYear + '\n')

    isOnlineStatus = True
    try:
        driver.find_element(By.CLASS_NAME, "x6s0dn4.xzolkzo.x12go9s9.x1rnf11y.xprq8jg.x9f619.x3nfvp2.xl56j7k.xv9rvxn.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x1gp4ovq.xdio9jc.x1h2mt7u.x7g060r.x10w6t97.x1td3qas.x6zyg47.x1xm1mqw.xpn8fn3.xtct9fg")
                # try to find green dot on avatar
    except NoSuchElementException:
        isOnlineStatus = False

    if isOnlineStatus == True:
        strStatus = f"{currentTime} 1"
    else:
       strStatus = f"{currentTime} 0"
    
    tracking.write(strStatus + '\n')

    tracking.close()

    if os.path.isfile(f"D:\\Code\\Python\\Data\\{saveFileName}.txt") == False:
        os.system(f"echo new > D:\\Code\\Python\\Data\\{saveFileName}.txt")  # Create new save data file with content "new" 

    os.system(f"type D:\\code\\python\\tracking.txt > D:\\code\\python\\data\\{saveFileName}.txt")
        # Copy data from tracking.txt to saveFileName.txt

    os.system("python -u D:\\Code\\Python\\Statistics.py")
    if os.path.isfile(f"D:\\Code\\Python\\Figure\\{saveFileName}.jpg") == False:
        os.system(f"echo new > D:\\Code\\Python\\Figure\\{saveFileName}.jpg")
    os.system(f"type D:\\code\\python\\figure.jpg > D:\\code\\python\\Figure\\{saveFileName}.jpg") 
        # Copy image from figure.jpg to saveFileName.jpg

    time.sleep(120)