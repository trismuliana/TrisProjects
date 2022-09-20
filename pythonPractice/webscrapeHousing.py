from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_ = "listing-search-item")

with open('Ahousing.csv', 'w', encoding='UTF8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)

    for item in lists:
        title = item.find('a', class_="listing-search-item__link--title").text.replace('\n','')
        location = item.find('div', class_="listing-search-item__sub-title").text.replace('\n','')
        price = item.find('div', class_="listing-search-item__price").text.replace('\n','')
        area = item.find('li', class_="illustrated-features__item--surface-area").text.replace('\n','')

        info = [title,location,price,area]
        thewriter.writerow(info)

       
