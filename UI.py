from logger import UserData

UD = UserData()

def interface():
    StartProg = True
    while StartProg:
        print("Производится работа с таблицами. Введите команду:\n 1-Вывод таблицы\n 2-Добавление новых значений\n 3-Изменение содержимого строки по коду\n 4-Удаление строки\n 5-Завершение работы")
        command = int(input('Введите число'))
        while command > 5 or command < 1:
            print("Неправильный ввод")
            command = int(input('Введите число - '))

        match command:
            case 1: UD.OutputData()
            case 2: InputData()
            case 3:
                pass
            case 4:
                pass
            case _:
                StartProg = False

def InputData():
    DataRow = list()
    HeadList = UD.InputData("Head")
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
                
                
