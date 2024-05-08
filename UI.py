from logger import UserData

UD = UserData()

def interface():
    StartProg = True
    while StartProg:
        print("Производится работа с таблицами. Введите команду:\n 1-Вывод таблицы\n 2-Добавление новых значений\n 3-Изменение содержимого строки по коду\n 4-Удаление строки\n 5-Сохранить изменения в фаил\n 6-Завершение работы")
        command = int(input('Введите число - '))

        #Проверка введеной команды
        while command > 6 or command < 1:
            print("Неправильный ввод")
            command = int(input('Введите число - '))

        #Список команд
        match command:
            case 1: print(UD.OutputData()) #Показ таблицы
            case 2: UD.InputData(InputCheck()) #Добавление в таблицу
            case 3: 
                IdRow = InputCheckId()
                print(f"Производится изменение строки:")
                print(UD.OutputData("Row",IdRow))
                UD.RowEdit(IdRow,InputCheck()) #Изменение в таблице
            case 4: 
                IdRow = InputCheckId()
                print(f"Производится удаление строки:")
                print(UD.OutputData("Row",IdRow))
                UD.DeleteRow(IdRow) #Удаление из таблицы
                print(f"Строка {IdRow} удалена, произведён перерасчет кода строк")
            case 5: 
                UD.SaveData() # Сохранение изменений в файл
                print(f"Произведено сохранение в фаил")
            case _: StartProg = False # Завершение работы программы
    
def InputCheck():
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
            print(f"Сохранены следующие изменения:\n{HeadList}\n{DataRow}")
            return DataRow

def InputCheckId():
    DataRowID = 1
    RowMax = UD.OutputData().shape[0]
    CheckWhileTrue = True
    while CheckWhileTrue:
        DataRowID = int(input("Введите код строки - "))
        if DataRowID > RowMax or DataRowID < 0:
            print("Неправильный ввод")
        else:
            CheckWhileTrue = False
            return DataRowID
