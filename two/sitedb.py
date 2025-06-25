import sqlite3
import os
from flask import Flask, render_template, flash, request, g

from two.fdatabase import FDataBase

# конфигурация (подключение базы данных)

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'qwertyuiop;'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():  # создаем функцию для соединения с базой данных
    con = sqlite3.connect(app.config["DATABASE"])
    con.row_factory = sqlite3.Row
    return con


def create_db():  # вспомогательная функция для создания таблицы в базе данных (потом она не участвует)
    db = connect_db()  # устанавливаем обьект соединения с базой
    with app.open_resource("sq_db.sql", "r") as f:
        db.cursor().executescript(f.read())  # выполняются запросы в базе, чтение
    db.commit()
    db.close()


def get_db():  # создаем функцию соединения с базой если оно не создано
    if not hasattr(g, 'link_db'):  # функция если соединение с базой данных не установлено, то его нужно установить
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index2.html', menu=dbase.get_menu())


@app.route("/add")
def add():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.get_menu())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('add_post.html', menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):  # функция если соединение с базой данных установлено, то его нужно будет потом закрыть
    if hasattr(g, "link_db"):
        g.link_db.close()


if __name__ == '__main__':
    app.run()