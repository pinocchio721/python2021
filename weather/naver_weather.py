from bs4 import BeautifulSoup
import requests
from pprint import pprint


# 1. 네이버 날씨를 get 해보자
html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)


# 2. parsing (의미있는걸로변화=변환하다)
soup = BeautifulSoup(html.text, 'html.parser') 
# pprint(soup)

# 3. soup에서 날씨정보만 가지고 싶어
data1 = soup.find('div',{'class':'weather_box'})
# print(type(data1))
# pprint(data1)

# 4. 주소 찾아줘
address = data1.find('span',{'class':'btn_select'}).text
print(f'현재위치 : {address}')

# 5. 온도 찾아줘
temp = data1.find('span', {'class': 'todaytemp'}).text
print(f'현재온도 : {temp}')

# 6. dd tag
data2 = data1.findAll('dd')

# 7. 미세먼지, 초미세먼지, 오존지수
dust = data2[0].find('span',{'class':'num'}).text
ultra_dust = data2[1].find('span',{'class':'num'}).text
ozone = data2[2].find('span',{'class':'num'}).text

print(f'미세먼지: {dust}')
print(f'초미세먼지: {ultra_dust}')
print(f'오존지수: {ozone}')