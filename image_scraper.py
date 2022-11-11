# import re
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urlparse
# import os


# def download_google(word):
# 	url = 'https://www.google.com/search?q=' + word + '&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'
# 	page = requests.get(url).text
# 	soup = BeautifulSoup(page, 'html.parser')
# 	for raw_img in soup.find_all('img'):
# 		link = raw_img.get('src')
# 		os.system("cd train/minecraft && wget " + link)

# word = input("Input key word: ")
# download_google(word)

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import urllib.request
from selenium.webdriver.common.keys import Keys


dog_breeds = ["pug",
    "pitbull",
    "chihuahua",
    "golden_retriever",
    "german_shepherd",
    "komondor"]

cat_breeds = ["russian blue cat", "siamese"]
for breed in cat_breeds:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com/')
    search = driver.find_element("name", 'q')    
    search.send_keys(f'{breed} cat breed images',Keys.ENTER)

    elem = driver.find_element("link text", 'Images')
    elem.get_attribute('href')
    elem.click()

    value = 0
    for i in range(70):

        print(f"{breed} load progress -> {i}")
        driver.execute_script('scrollBy("+ str(value) +",+500);')
        value += 500
        time.sleep(0.420)

    elements = driver.find_elements('xpath', '//img[contains(@class,"rg_i")]')
    count = 0
    for i in elements:
        src = i.get_attribute('src')
        try:
            if src != None:
                src = str(src)
                count += 1
                print(f'img count -> {count}')
                urllib.request.urlretrieve(src, os.path.join(f'cat_breed/{breed}/',f'{breed}'+str(count)+'.jpg'))
            else:
                raise TypeError
        except TypeError:	
            pass
