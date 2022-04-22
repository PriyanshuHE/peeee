import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.hk01.com/')
print(r)
soup  = BeautifulSoup(r.content,'html.parser')
s = soup.find('div', class_='y26340-1 cPcZEY')
print(s)
lines = s.find_all('span')
print(lines)
# o4febr-0 euMltm app-wrapper'