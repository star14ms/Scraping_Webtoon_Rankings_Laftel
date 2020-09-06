from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time, csv

driver = webdriver.Chrome(r'[driver path here]')
driver.get('https://laftel.net/rank/webtoon')
driver.implicitly_wait(5)

# 스크롤 높이 가져옴
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(5)
    time.sleep(1)

    # 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height: # 더 이상 안 내려가지면 while문 통과
      break 
    last_height = new_height

ranks = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]').text

webtoonRanks = ranks.replace('\n',' ').replace('점 ','점\n')

with open('웹툰 인기 순위_라프텔.txt', 'w') as file: # 메모장에 기록
  file.write(webtoonRanks)
print('\n' + webtoonRanks + '\n')


webtoons = []
list = ranks.replace('\n',',').replace('점,','점/').split('/')
for webtoon in list:
  webtoons.append(webtoon.split(','))
# print('\n' + str(webtoons) + '\n')

with open("웹툰 인기 순위_라프텔.csv", mode="w") as file: # csv파일에 기록
  writer = csv.writer(file)
  writer.writerow(['순위', '제목', '점수'])
  for webtoon in webtoons:
    writer.writerow(webtoon)