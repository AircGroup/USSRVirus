import os
import uuid
import random
import win32console

def subprocess():
    win32console.FreeConsole() #Frees subprocess from using main console
    win32console.AllocConsole() #Creates new console and all input and output of subprocess goes to this new console
    os.system('color 4')
    print("Начат взлом Запада")
    print(f"Подбор пароля к сети 192.168.0.1")
    per = uuid.uuid4()
    final = uuid.uuid4()
    asiiList = [chr(i) for i in range(128)]
    while True:
        print(f"Проверка пароля {per}")

        per = uuid.uuid4()
        if random.randint(0, 2) == 0:
            print("Подошел. Ставим Бэкдоор.")
            print("Попытка не получилось. Код безопасности ресетнут.")
            print("Подбираем новый Хэш-ключ. Пожалуйста не перезагружайте систему.")
        

        print(f"Не подходит")