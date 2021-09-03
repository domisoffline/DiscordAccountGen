from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import pyautogui
import requests
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def sendKeys(object, str):
    for char in str:
        object.send_keys(char)
        time.sleep(random.uniform(0.02,0.2))

def writeKeys(str):
    for char in str:
        pyautogui.write(char)
        time.sleep(random.uniform(0.01,0.7))

usernames = ['BigMoney123', 'JoeBidenFan33', 'ObamaIsMyHomie']
passwords = ['Mailman143!', 'MegaManFan135', 'ObamaLand444?', 'BigSexMan5555%']
emails = []
with open('emails.txt', 'r') as f:
    for line in f:
        emails.append(line.strip())
driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
driver.get("http://discord.com/register")
email = driver.find_element_by_class_name("inputDefault-_djjkz")
sendKeys(email, str(random.choice(emails)))

username = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/form/div/div/div[2]/div/input')
used_email = str(random.choice(usernames))
sendKeys(username, used_email)

password = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/form/div/div/div[3]/div/input')
used_pass = str(random.choice(passwords))
sendKeys(password, used_pass)

actions = ActionChains(driver)
month = driver.find_elements_by_class_name('css-1hwfws3')[0].click()
writeKeys(str(random.randint(1,12)))
pyautogui.press('enter')

writeKeys(str(random.randint(1,25)))
pyautogui.press('enter')

writeKeys(str(random.randint(1975,2000)))
pyautogui.press('enter')

submit = driver.find_element_by_class_name('button-3k0cO7').click()
time.sleep(random.uniform(0.07,0.4))

input("\nPlease Complete Captcha. When finished press ENTER KEY.\n")

time.sleep(random.uniform(0.07,0.4))

print(f"\nDone.\n\nUsed Email: {used_email}\nUsed Password: {used_pass}")