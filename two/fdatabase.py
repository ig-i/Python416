class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"  # получаем все данные из таблицы mainmenu
        try:
            self.__cur.execute(sql)  # метод выполняет sql запросы
            res = self.__cur.fetchall()  # получаем все данные из запроса
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []