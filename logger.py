import pandas as pd

class UserData:

    def __init__(self):
        self.DataCSV = pd.read_csv("DataUser.csv")

    def OutputData(self, DataHaed = "Full"):
        if DataHaed == "Head":
            return self.DataCSV.columns.tolist()
        else: return self.DataCSV.head()
    
    def InputData(DataToSave):
        pass