import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com"


def get_quotes_from_web():
    """
    Функция должна:
    1. Сделать GET-запрос по адресу URL.
    2. Если статус ответа не 200, вернуть пустой список.
    3. Если всё ок, распарсить HTML с помощью BeautifulSoup.
    4. Найти все блоки цитат (это div с классом "quote").
    5. Из каждого блока извлечь:
       - Текст цитаты (span с классом "text")
       - Автора (small с классом "author")
    6. Вернуть список словарей формата:
       [{"text": "Цитата 1", "author": "Автор 1"}, ...]
    """

    # =================================================================================
    # ЗАДАНИЕ 2: Реализуйте логику парсинга
    # [Если сложно - см. файл hints/2_parser_hint.txt]
    # =================================================================================

    print(f"Парсинг сайта {URL}...")

    response = requests.get(URL) #загружает страницу
    if response.status_code != 200: #проверяем что страница правильно загружена
        print("Ошибка подключения")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []

    for block in soup.find_all("blockcoote",class_="col-md-8"): # все цитаты
      quote_text = block.find("span", {"class": "text"}).get.text() #Текст цитаты
      author = block.find("small", {"class": "author"}).get.text( ) #автор

      quotes.append({"text": quote_text, "author": author})
   
    return quotes
   
 
