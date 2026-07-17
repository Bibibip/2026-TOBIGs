import requests
from bs4 import BeautifulSoup

url = "https://kin.naver.com/search/list.nhn?query=파이썬"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    #title = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a')
    ul = soup.select_one('ul.basic1')

    titles = ul.select('li > dl > dt > a')
    for title in titles:
        print(title.get_text())

else:
    print(f"Error: {response.status_code}")