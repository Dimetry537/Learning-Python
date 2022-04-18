print("Всем приветы в этом чате")

speaker = "Миша"
duration = 130
duration_hours = round(duration / 60, 2)

print(f"Наш эфир будет длиться: {duration} минут, {duration_hours} часов")
print(f"Ведет эфир: {speaker}")

if duration_hours > 2:
  print("Запасайтесь печеньками, эфир будет длинный")
else:
  print("На чиле, на расслабоне")

visitors = ["Artemy Andreev", "Denis Petrov", "Oleg Kushnir", "Nikita Raenenko"]

for visitor in visitors:
    print(f"Приветствует уважаемого слушателя {visitor}")

# Словарь / Dictionary
webinar = {
    "speaker": "Миша",
    "duration": 130,
    "name": "Мессенджер на Пайтон"
}

print(f"Тема эфира: {webinar['name']} ")


