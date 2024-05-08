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
            case 3: DataChange()
            case 4:
                pass
            case 5: UD.SaveData()
            case _:
                StartProg = False

def InputData():
    UD.InputData(InputCheck())


def DataChange():
    DataRowID = 1
    RowMax = UD.OutputData().shape[0]
    CheckWhileTrue = True
    while CheckWhileTrue:
        DataRowID = int(input("Введите код строки которую необходимо изменить - "))
        if DataRowID > RowMax or DataRowID < 0:
            print("Неправильный ввод")
        else:
            CheckWhileTrue = False

    UD.RowEdit(DataRowID,InputCheck())
    
    
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
                
