import requests
from bs4 import BeautifulSoup

url='https://course.nctu.edu.tw/index.asp'
html=requests.get(url).text
sp=BeautifulSoup(html,'lxml')

lessons=sp.find_all('font')

for lesson in lessons:
    print(lesson.text)