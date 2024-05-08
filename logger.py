import pandas as pd

class UserData:

    def __init__(self):
        self.DataCSV = pd.read_csv("DataUser.csv")

    #Блок вывода таблицы или её частей
    def OutputData(self, OutputMethod = "Full",RowIndex = 0):
        if OutputMethod == "Full": 
            return self.DataCSV.head()
        elif OutputMethod == "Head":
            return self.DataCSV.columns.tolist()
        elif OutputMethod == "Row":
            return self.DataCSV.loc[RowIndex]
            
    
    #Блок сохранение\изменение данных
    def InputData(self,DataToSave): self.DataCSV.loc[ len(self.DataCSV.index )] = DataToSave
    def RowEdit(self,RowIndex,RowList): self.DataCSV.loc[RowIndex] = RowList
    def SaveData(self): self.DataCSV.to_csv("DataUser.csv",index=False)