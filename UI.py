from logger import UserData

UD = UserData()

def interface():
    StartProg = True
    while StartProg:
        print("Производится работа с таблицами. Введите команду:\n 1-Вывод таблицы\n 2-Добавление новых значений\n 3-Изменение содержимого строки по коду\n 4-Удаление строки\n 5-Сохранить изменения в фаил\n 6-Завершение работы")
        command = int(input('Введите число - '))
        while command > 6 or command < 1:
            print("Неправильный ввод")
            command = int(input('Введите число - '))

        match command:
            case 1: print(UD.OutputData())
            case 2: InputData()
            case 3:
                pass
            case 4:
                pass
            case 5: UD.SaveData()
            case _:
                StartProg = False

def InputData():
    DataRow = list()
    HeadList = UD.OutputData("Head")
    CheckWhileTrue = True
    while CheckWhileTrue:
        print("Введите данные следующем формате:")
        print(",".join(HeadList))
        DataRow = input().split(',')
        if(len(DataRow) != len(HeadList)):
            print("Неправильный ввод")
        else: 
            CheckWhileTrue = False
            UD.InputData(DataRow)
            print(f"Сохранены следующие изменения:\n{HeadList}\n{DataRow}")
                
                
