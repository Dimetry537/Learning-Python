from flask import Flask, request, render_template
from datetime import datetime

application = Flask(__name__)  # Создаем Flask-приложение
# Начинаем писать мессенджер
all_messages = []  # Список всех сообщений


@application.route("/chat")
def display_chat():
    return render_template("form.html")  # Показываем файл из папки templates


@application.route("/")
def index_page():
    return "Hello, welcome to Skillbox Chat"


@application.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


@application.route("/send_message")
def send_message():
    # name, text ?
    # Получаем информацию от пользователя
    sender = request.args["name"]
    text = request.args["text"]

    # Добавляем сообщение в список
    add_message(sender, text)
    return "OK"


def add_message(sender, text):
    # 1. Подготовить словарь с данными сообщения
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M:%S"),
    }
    # 2. Добавить получившийся словарь в список всех сообщений
    all_messages.append(new_message)


def print_message(mess):
    print(f"[{mess['sender']}]: {mess['text']} / {mess['time']}")


# add_message("Миша", "Всем приветы")
# add_message("Вася", "Библиотека Flask скачать бесплатно")
#
# for message in all_messages:
#     print_message(message)

application.run()  # Запускаем приложение


#  ДЗ:
#  Предусмотреть ограничения для имени и текста (валидация данных) в фунции add_message

#  День 3:
#  Подгтовить код к размещению на хостинге
#  Настроить хостинг и запустить там чат
#  Сохранение сообщений в файл

