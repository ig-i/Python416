from view2 import UserInterface
from model2 import ArticleModel


class Controller:
    def __init__(self):
        self.article_model = ArticleModel()  # это связь с документом model
        self.user_interface = UserInterface()  # это связь с документом view

    def run(self):
        answer = None
        while answer != 'q':                                 # выход из программы (если пользователь введет q)
            answer = self.user_interface.wait_user_answer()  # ввод польз. данных метод в классе UserInterface (view.py)
            self.check_user_answer(answer)                   # возвращаем то что пользователь ввел из view.py

    def check_user_answer(self, answer):  # проверить пользовательский ответ (что пользователь выбрал)
        if answer == "1":                 # пользователь вводит данные (создание статьи)
            article = self.user_interface.add_user_article()  # запрашиваем инф. от пользоваетеля по статье (из view)
            self.article_model.add_article(article)  # сохраняем данные в хранилище (model) класса ArticleModel
        elif answer == "2":                          # просмотр статьи
            articles = self.article_model.get_all_articles()  # обращаемся к модели чтобы вернуть все статьи
            self.user_interface.show_all_articles(articles)  # обращаемся к view и показываем данные (все статьи)
        elif answer == "3":
            article_title = self.user_interface.get_user_article()
            try:
                article = self.article_model.get_single_article(article_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(article_title)
            else:
                self.user_interface.show_single_article(article)
        elif answer == "4":  # удаление фильма
            article_title = self.user_interface.get_user_article()
            try:
                title = self.article_model.remove_article(article_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(article_title)
            else:
                self.user_interface.remove_single_article(title)
        elif answer == "q":  # выход из программы
            self.article_model.save_data()
        else:
            self.user_interface.show_incorrect_answer_error(answer)
