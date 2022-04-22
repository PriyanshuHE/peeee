# import requests
# from bs4 import BeautifulSoup
# r = requests.get('https://hk.on.cc/hk/intnews/index.html')
# print(r)
# soup  = BeautifulSoup(r.content,'html.parser')
# s = soup.find('div', class_='leftside')
# print(s)
# lines = s.find_all('p')
# print(lines)
# # o4febr-0 euMltm app-wrapper'y26340-1 cPcZEY
# sc-5vyyvj-0
n = int(input("Enter your no"))
if n%1==0 or n%n==0:
    print("p")
else:
    print("np")    
     