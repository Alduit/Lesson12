import csv

class UserData:

    def __init__(self,DataDict):
        self.__DataDict = DataDict

    def PrintData():
        print(*self.__DataDict)

    def InputData():
        return self.__DataDict

    def UpdateUserData():
        with open("DataUser.csv",encoding='utf-8') as r_file:
            