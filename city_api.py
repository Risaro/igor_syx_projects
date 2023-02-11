import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {'user-agent':'Mozilla/5.0'}
    respone = requests.get(url, headers=headers)
    html = respone.text
    return  html
#get_html('https://sinoptik.ua')
def get_weather_now(city):
    url = f'https://sinoptik.ua/погода-{city}'
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    try:
        temp = soup.find('p', 'today-temp').get_text(strip=True)
        decription = soup.find('div', 'description').get_text(strip=True)
        print(temp)
        print(decription)
    except:
        print(f'Городд {city} не обнаружен ')
#text = input('Введите город которому не угрожают бомбардировкой')
#get_weather_now(text)
def custom_site(url):
    html = get_html(url)
    soup = BeautifulSoup(html,'html.parser')
    try:
        custom_text = soup.find('table', 'border')
        print(custom_text)
    except:
        print('ошибка')
custom_site('https://ru-minecraft.ru/krafting-v-minecraft.html#new116')