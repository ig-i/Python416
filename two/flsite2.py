from flask import Flask, render_template, request

app = Flask(__name__)

menu = [
    {"name": "Страница новостей", "url": "index"},
    {"name": "Новости сегодня", "url": "about"},
    {"name": "Прислать новость", "url": "contact"}
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index2.html",
                           title="Страница новостей", menu=menu)                            # подключаем страницу html


@app.route("/about")
def about():
    return render_template("about2.html", title="Новости сегодня", menu=menu)  # подключаем страницу html


@app.route("/profile/<int:username>")
def profile(username):
    return f"Пользователь: {username}"


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        print(request.form)
        print(request.form['email'])
    return render_template("contact2.html", title="Прислать новость", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)