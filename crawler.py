from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.chrome.options import Options
import sys
import time 

options = Options()             
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webdriver_path = 'C:\\Users\\hou\\Desktop\\allison_code\\python\\chromedriver.exe'
WIKI_URL = 'https://en.wikipedia.org/wiki/Ruel_(singer)'
something = driver.get(WIKI_URL)

# time.sleep(5)

#名字
name = driver.find_element(By.CSS_SELECTOR, '.nickname')
_class = name.text
# print(_class)

#照片
picture = driver.find_element(By.CSS_SELECTOR, 'a.image img')
src = picture.get_attribute('src')
# print(src)


info = {}
trs = driver.find_elements(By.CSS_SELECTOR, "table.infobox tr")
for tr in trs[3:]:
    # print(tr.text)
    th = tr.find_element(By.CSS_SELECTOR, "th ")
    #Born
    if th.text == "Born" :
        td =  tr.find_element(By.CSS_SELECTOR, "td")
        # print(td.text)
        info["Born"] = td.text

        #生日
        born = info["Born"]
        birthday = born[ : born.index("\n")]
        print(birthday)
        quit()



    #Origin 
    if th.text == "Origin" :
        td = tr.find_element(By.CSS_SELECTOR, "td")
        # print(td.text)
        info["Origin"] = td.text

    #Genres  
    if th.text == "Genres":
        # 作法1 (標準版)
        a_s = tr.find_elements(By.CSS_SELECTOR, "td li a")
        # loop for 版
        genres = []
        for a in a_s:
            genres.append(a.text)


        # # loop for 數數版 
        # genres = []
        # for c in range(0, len(a_s)):
        #     genres.append(a_s[c].text)

        
        # # loop while版 
        # genres = []
        # c = 0
        # while c < len(a_s):
        #     genres.append(a_s[c].text)
        #     c += 1
        
        info['Genres'] = genres
        
        # 作法2 (偷吃步法)
        # td = tr.find_element(By.CSS_SELECTOR, "td")
        # print(td.text)

   
print(info)
driver.close()
