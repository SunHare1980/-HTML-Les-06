# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
url = "https://www.divan.ru/kursk/category/svet"
driver.get(url)
parsed_data = []

for element in driver.find_elements(By.TAG_NAME, "div"):
    cl = element.get_attribute("class")
    if cl.find ('_Ud0k') == 0:
        link = ''
        price = ''
        name = ''
        link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
        element.find_element(By.TAG_NAME, 'a').get_attribute('href')
        for element1 in element.find_elements(By.TAG_NAME, "div"):
            cl2 = element1.get_attribute("class")
            if cl2 == 'pY3d2':
                price = element1.find_element(By.TAG_NAME, "span").text
                # price = element1.text.split('\n', 1)
            if cl2 == 'lsooF':
                # name = element1.text
                name = element1.find_element(By.TAG_NAME, "span").text
        parsed_data.append([name, price, link])


driver.quit()

print(parsed_data)
# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("hh.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)