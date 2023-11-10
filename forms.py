from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
load_dotenv() 
email=os.getenv("email")
pwd=os.getenv("pwd")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://forms.gle/XYbwmUrfQPR8o8496")#A sample G-Form link
def user():
    fname=driver.find_element(by=By.NAME,value="identifier")
    but=driver.find_element(by=By.CSS_SELECTOR,value="#identifierNext")
    fname.send_keys(email)#Your email address
    but.click()
def pwd():
    fiel=driver.find_element(by=By.NAME,value="Passwd")
    butt = driver.find_element(by=By.CSS_SELECTOR,value="#passwordNext")
    fiel.send_keys(pwd)#Your password
    butt.click()
def nex():
    element = driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
    element.click()
def ans():
    fir=driver.find_element(By.XPATH,"//*[@id='i11']")
    fir.click()
    fir1=driver.find_element(By.XPATH,"//*[@id='i30']")
    fir1.click()
    fir2=driver.find_element(By.XPATH,"//*[@id='i40']")
    fir2.click()
    fir3=driver.find_element(By.XPATH,"//*[@id='i56']")
    fir3.click()
    fir4=driver.find_element(By.XPATH,"//*[@id='i75']")
    fir4.click()
    fir5=driver.find_element(By.XPATH,"//*[@id='i85']")
    fir5.click()
    fir6=driver.find_element(By.XPATH,"//*[@id='i107']")
    fir6.click()
    fir7=driver.find_element(By.XPATH,"//*[@id='i126']")
    fir7.click()
    fir8=driver.find_element(By.XPATH,"//*[@id='i136']")
    fir8.click()
    fir9=driver.find_element(By.XPATH,"//*[@id='i152']")
    fir9.click()
    fir10=driver.find_element(By.XPATH,"//*[@id='i168']")
    fir10.click()
    fir11=driver.find_element(By.XPATH,"//*[@id='i184']")
    fir11.click()
    fir12=driver.find_element(By.XPATH,"//*[@id='i200']")
    fir12.click()
    fir13=driver.find_element(By.XPATH,"//*[@id='i219']")
    fir13.click()
    fir13=driver.find_element(By.XPATH,"//*[@id='i238']")
    fir13.click()
    fir14=driver.find_element(By.XPATH,"//*[@id='i251']")
    fir14.click()
    fir15=driver.find_element(By.XPATH,"//*[@id='i270']")
    fir15.click()
    fir16=driver.find_element(By.XPATH,"//*[@id='i277']")
    fir16.click()
    fir17=driver.find_element(By.XPATH,"//*[@id='i293']")
    fir17.click()
    fir18=driver.find_element(By.XPATH,"//*[@id='i315']")
    fir18.click()
    fir19=driver.find_element(By.XPATH,"//*[@id='i331']")
    fir19.click()
    fir20=driver.find_element(By.XPATH,"//*[@id='i347']")
    fir20.click()
    fir21=driver.find_element(By.XPATH,"//*[@id='i357']")
    fir21.click()
    fir22=driver.find_element(By.XPATH,"//*[@id='i379']")
    fir22.click()
    fir23=driver.find_element(By.XPATH,"//*[@id='i398']")
    fir23.click()
    bat=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div[2]")
    bat.click()
user()
# driver.implicitly_wait(10)
# pwd()
# driver.implicitly_wait(10)
# nex()
# driver.implicitly_wait(10)
# ans()

