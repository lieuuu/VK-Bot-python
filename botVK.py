import vk_api #модуль работы с vk-api
import json #модуль работы с json 
import time #модуль работы со временем
from vk_api.longpoll import  VkLongPoll,VkEventType
key = "API - VK key in the group"
vk_session = vk_api.VkApi(token = key)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
users = vk.users
def counter(user):
    file = open("stats.json","r") # "r" - read , "w" - write
    data = json.loads(file.read())
    data["counter"] += 1
    if user not in data["users"]:
        data["users"].append(user)
    file = open("stats.json","w") # "r" - read , "w" - write
    file.write(json.dumps(data))
def getCounter():
    file = open("stats.json", "r")  # "r" - read , "w" - write
    data = json.loads(file.read())
    return data["counter"]
def getUsers():
    file = open("stats.json", "r")  # "r" - read , "w" - write
    data = json.loads(file.read())
    return len(data["users"])
def riddleFunction():# Чертеж прослушки
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            counter(event.user_id)
            if event.text.lower().find("ответ на тест") <= -1: #можно использовать несколько ответов, но будут они писаться через ""
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=time.time(),
                    message="Молодец , у тебя все получилось!") #результат твоего ответа
                return 1
            elif (event.text.lower() == 'подсказка'): #подсказка в случае неправильного ответа
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=time.time(),
                    message="", #сообщение(подсказка)
                    attachment = "") #ссылка на картинку, видео(подсказка)
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=time.time(),
                    message="Не верный ответ! Можешь запросить подсказку") #прозьба о запросе подсказки

def moodFunction():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=time.time(),
                    message="Не понимаю тебя , повтори пожалуйста") #бот не понимает твоих действий 




for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        counter(event.user_id)
        if(event.text.lower()=='текст'): #значение, которое вы хотите задать
            keys = open("keys.json" , "r" , encoding="UTF-8").read()
            name = users.get(user_ids=event.user_id, fields='city')[0]['first_name']
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="текст" + name + "текст", keyboard = keys) #можно использовать как приветствие бота при выполнение значения
            moodFunction()
        elif(event.text.lower() == "!обработка сообщений"): #сколько бот обработал сообщений
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message=str(getCounter()) + " вот столько. " + str(getUsers()) + " - столько пользователей мне написало") #получения информации
        elif (event.text.lower() == "где ты живешь"): #значение, которое может выводить ваш город
            try:
                city = users.get(user_ids=event.user_id, fields='city')[0]['city']['title']
            except:
                city = "который не указан" #город не высвечивается, если он у вас не указан в профиле вк
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="Ты из города " + city) #город высвечивается в процессе выполнения значения

        elif (event.text.lower() == "тест"): #значение, которое вы хотите задать(в этой строке можно сделать маленький тест). Строчка 85 относится к строчке 30
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="текст") #вопрос к тесту выводящийся в процессе выполнения значения
            riddleFunction()#Запуск прослушки
        elif (event.text.lower() == "текст"): #значение, которое вы хотите задать
            name = users.get(user_ids=event.user_id, fields='city', name_case="dat")[0]['first_name']
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="") #вообщение, которое вы получите в процессе выплнения значения(текст)
        elif (event.text.lower() == "текст"): #значение, которое вы хотите задать
            name = users.get(user_ids=event.user_id, fields='city', name_case="dat")[0]['first_name']
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                attachment = "ссылка") #сообщение, которое вы получите в процессе выполнения значения(фотографи или видео(ссылка))
        elif (event.text.lower() == "текст"): #значение, которое вы хотите задать
            name = users.get(user_ids=event.user_id, fields='city', name_case="dat")[0]['first_name']
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="текст") #сообщение, которое вы поулчите в процессе выполнения значения(текст)
        elif (event.text.lower() == "!unity"): #значение, которое ввы хотите задать
            name = users.get(user_ids=event.user_id, fields='city', name_case="dat")[0]['first_name']
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="") #сообщение, которе вы получите в процессе выполнения значения(текст)
        else:
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="Не понял , что ты написал") #бот не понимает что ты написал

