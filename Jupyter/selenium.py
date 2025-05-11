# %%
# %pip install selenium

# %%
# %pip install webdriver_manager

# %%
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# options 객체를 만들지 않으면 실행시 브라우저 창이 꺼짐
options = Options()
options.add_argument("--start-maximized") #창크기 최대화
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)  

url = "https://www.naver.com/"
driver.get(url)

# %%
# 검색어 입력
driver.find_element(By.ID, 'query').send_keys('크리스마스 캐롤')
# 검색어 입력 후 2초 대기 
time.sleep(2)

# 검색버튼 클릭
search_btn = driver.find_element(By.CSS_SELECTOR,'#search-btn')
search_btn.click()

# # 엔터 쳐서 검색
# driver.find_element(By.ID,'query').send_keys(Keys.ENTER)
# time.sleep(2)

# 스크린샷
driver.save_screenshot('./crawling/스팩.png')

driver.quit()

# %%
search_item = input('상품명 또는 브랜드 입력 : ')

options = Options()
options.add_argument("--start-maximized") #창크기 최대화
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)  

url2 = "https://shopping.naver.com/ns/home"
driver.get(url2)

driver.find_element(By.CSS_SELECTOR, '#gnb-gnb > div._gnb_header_area_nfFfz > div > div._gnbContent_gnb_content_JUwjU > div._gnbSearch_gnb_search_ULxKx > form > div > div > div > div > input').send_keys(search_item)
time.sleep(2)

search_btn2 = driver.find_element(By.CSS_SELECTOR, '#gnb-gnb > div._gnb_header_area_nfFfz > div > div._gnbContent_gnb_content_JUwjU > div._gnbSearch_gnb_search_ULxKx > form > div > div > div > div > button._searchInput_button_search_wu9xq._nlog_click')
search_btn2.click()
time.sleep(2)

current_height = driver.execute_script("return window.scrollY")

count = 0

while True:
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)
    time.sleep(1)
    
    scrolled_height = driver.execute_script("return window.scrollY")
    
    if (current_height == scrolled_height):
        break
    
    if count > 1:
        break
    count+=1
    
    current_height = scrolled_height

import requests
from bs4 import BeautifulSoup
import openpyxl

responce = requests.get(f'https://search.shopping.naver.com/ns/search?query={search_item}')
html = responce.text
soup = BeautifulSoup(html, 'html.parser')

all_li = soup.select('ul.compositeCardList_product_list__Ih4JR')
print(all_li)


# %%
from bs4 import BeautifulSoup

# 사용자 입력
search_item = input('상품명 또는 브랜드 입력: ')

# Selenium 설정
options = Options()
options.add_argument("--start-maximized")  # 창 최대화
options.add_experimental_option('detach', True)  # 브라우저 닫지 않음
driver = webdriver.Chrome(options=options)

# 네이버 쇼핑 페이지 열기
url = "https://shopping.naver.com/home"
driver.get(url)

# 검색창에 검색어 입력
driver.find_element(By.CSS_SELECTOR, '#gnb-gnb > div._gnb_header_area_nfFfz > div > div._gnbContent_gnb_content_JUwjU > div._gnbSearch_gnb_search_ULxKx > form > div > div > div > div > input').send_keys(search_item)
time.sleep(3)  # 페이지 로딩 대기

# 검색어 클릭
search_btn2 = driver.find_element(By.CSS_SELECTOR, '#gnb-gnb > div._gnb_header_area_nfFfz > div > div._gnbContent_gnb_content_JUwjU > div._gnbSearch_gnb_search_ULxKx > form > div > div > div > div > button._searchInput_button_search_wu9xq._nlog_click')
search_btn2.click()
time.sleep(2)

# 스크롤 다운
current_height = driver.execute_script("return window.scrollY")

count = 0

while True:
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)
    time.sleep(1)
    
    scrolled_height = driver.execute_script("return window.scrollY")
    
    if (current_height == scrolled_height):
        break
    
    if count > 1:
        break
    count+=1
    
    current_height = scrolled_height

import openpyxl
# 엑셀 만들기
wb = openpyxl.Workbook()

# 워크시트 만들기
ws = wb.active
ws.title = '쇼핑'

# 데이터 추가하기
ws.append(['상품명', '판매가', 'url'])

# 엑셀 저장하기
filePath = 'shopping.xlsx'

products = driver.find_elements(By.CSS_SELECTOR, '.basicProductCard_basic_product_card__TdrHT')

for product in products:
    # print("product",product)
    t = product.find_element(By.CSS_SELECTOR, '.basicProductCardInformation_title__Bc_Ng').text
    print(t)
    p = product.find_element(By.CSS_SELECTOR, '.priceTag_inner_price__TctbK').text.split()[0]    
    print(p)
    a = product.find_element(By.CSS_SELECTOR, '.basicProductCard_link__urzND')
    # print(a)
    l = a.get_attribute("href")
    print(l)
    ws.append([t, p, l])

wb.save(filePath)


