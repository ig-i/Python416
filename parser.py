import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""  # статические свойства
    res = []

    def __init__(self, url, path):
        self.url = url     # приходит ссылка на адрес из main - https://www.ixbt.com/live/index/news/
        self.path = path   # приходит имя документа из main - "news.txt"

    def get_html(self):
        req = requests.get(self.url).text  # получили данные по ссылке
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        news = self.html.find_all("div", class_="caption") # возвращает список однотипных div с классом в виде списка
        for item in news:
            title = item.find("h3").text  # получили содержимое всех тегов h3 (все заголовки новостей) в виде текста
            href = item.find("a").get('href')  # получили содержимое тега а и ссылки в нем
            author = item.find("a", class_="topic-info-author-link").text.strip() # получили авторов и избавились от пробелов

            self.res.append({
                "title": title,
                "href": href,
                "author": author
            })
        # print(self.res)                # вывели список из словарей полученной информации
    def save(self):
        with open(self.path, "w") as f:  # передаем информацию на запись в документ "news.txt"
            i = 1
            for item in self.res:
                f.write(f"Новость №{i}\n\nНазвание: {item['title']}\nСсылка: {item['href']}"
                        f"\nАвтор: {item['author']}\n\n{'*' * 20}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()


