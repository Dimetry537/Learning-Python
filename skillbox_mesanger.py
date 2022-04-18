from time import time


all_messages = []

def add_message(sender, text):
  # 1. Подготовить словарь с данными сообщения
    new_message = {
      "sender": sender,
      "text": text,
      "time": time.time(),  # ToDo: Здесь должно быть текущее время
  }
  # 2. Добавить получившийся словарь в список всех сообщений
    all_messages.append(new_message)


def print_message(mess):
    print(f"[{mess['sender']}]: {mess['text']} / {mess['time']}")

add_message("Миша", "Всем приветы")
add_message("Вася", "Библиотека Flask скачать бесплатно")

for message in all_messages:
    print_message(message)

# todo: 