import vk_api
import json
import time
from vk_api.longpoll import  VkLongPoll,VkEventType
key = "304edfe291a39e4be153976914532de6a24905e4b5e102805a7d31be4d3f045a4aca260e038b234d46873"
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
            if event.text.lower().find("python" "" "пайтон") <= -1:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=time.time(),
                    message="Молодец , у тебя все получилось!")
                return 1
            elif (event.text.lower() == 'подсказка'):
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=time.time(),
                    message="змея!",
                    attachment = "photo-196126300_457239023")
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=time.time(),
                    message="Не верный ответ! Можешь запросить подсказку")

def moodFunction():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=time.time(),
                    message="Не понимаю тебя , повтори пожалуйста")




for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        counter(event.user_id)
        if(event.text.lower()=='!меню'):
            keys = open("keys.json" , "r" , encoding="UTF-8").read()
            name = users.get(user_ids=event.user_id, fields='city')[0]['first_name']
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="Привет, " + name + " ,я бот, который стараеться любым способом помочь разработчикам игр!!!"
                                           "\nВот мой список команд:"
                                           "\n!меню"
                                           "\n!UE5"
                                           "\n!UE4"
                                           "\n!UE5t"
                                           "\n!Топ 10 ассетов UE4"
                                           "\n!Топ 10 ассетов Unity"
                                           "\nДругие команды:"
                                           "\n!Обработка сообщений"
                                           "\n!Связь с администрцией"
                                           "\n!Где я живу?",
                                            keyboard = keys)
            moodFunction()
        elif(event.text.lower() == "!обработка сообщений"):
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message=str(getCounter()) + " вот столько. " + str(getUsers()) + " - столько пользователей мне написало")
        elif (event.text.lower() == "!где я живу?"):
            try:
                city = users.get(user_ids=event.user_id, fields='city')[0]['city']['title']
            except:
                city = "который не указан"
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="Ты из города " + city)

        elif (event.text.lower() == "хочу тест"):
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="1. На каком языке был сделан Battlefield?")
            riddleFunction()#Запуск прослушки
        elif (event.text.lower() == "!связь с администрацией"):
            name = users.get(user_ids=event.user_id, fields='city', name_case="dat")[0]['first_name']
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="Администрация получила оповещение! В скором времени они вам ответят."
                        " Если хотите что бы они ответили быстрее перейдите по ссылке: \nvk.com/inval1dsyntax")
        elif (event.text.lower() == "!ue5t"):
            name = users.get(user_ids=event.user_id, fields='city', name_case="dat")[0]['first_name']
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                attachment = "video-176128467_456239173")
        elif (event.text.lower() == "!ue4"):
            name = users.get(user_ids=event.user_id, fields='city', name_case="dat")[0]['first_name']
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="UE4 - игровой движок, разрабатываемый и поддерживаемый компанией Epic Games. Один из самых популярных игровых движков."
                        "\nЯзык программирования: C++"
                        "\nПоддерживает: Windows 7+ ; MacOS 10.9.2+"
                        "\nЗанимает места: 22 ГБ (с установками пакетов и ассетов требуеться не меньше 100гб свободного места"
                        "\nТребования к железу:"
                        "\n1.64-битная операционная система"
                        "\n2.Четырехъядерный процессор частотой от 2.5 ГГцNVIDIA GeForce 470 GTX или AMD Radeon 6870 HD и выше"
                        "\n3.8ГБ оперативной памяти")
        elif (event.text.lower() == "!unity"):
            name = users.get(user_ids=event.user_id, fields='city', name_case="dat")[0]['first_name']
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="Unity — межплатформенная среда разработки компьютерных игр, разработанная американской компанией Unity Technologies."
                        "\nЯзык программирования: C#"
                        "\nПоддерживает: Windows7+ ; MacOS10.9.2+ ; Linux"
                        "\nЗанимает места: 14,6 гб"
                        "\nТребования к железу:"
                        "\n1.Процессор с поддержкой SSE2"
                        "\n2.Видеокарта с поддержкой DirectX 9 (модель шейдера 3.0) или DirectX 11 с поддержкой возможностей уровня 9.3.")
        else:
            vk.messages.send(
                user_id=event.user_id,
                random_id=time.time(),
                message="Не понял , что ты написал")

