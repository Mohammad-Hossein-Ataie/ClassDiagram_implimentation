#In the Name of God
import csv
import time
class User:
    # init method or constructor 
    def __init__(self, name, id):
        self.name = name
        self.id = id
    # Sample Method 
    def say_hi(self):
        print('Wellcome,', self.name, '!')
class Request( object ):    
        def __init__(self, name, idnumber):   
                self.name = name
                self.idnumber = idnumber
        def display(self):
                print(self.name)
                print(self.idnumber)
# child class
class Transportation( Request ):           
        def __init__(self, name, idnumber, type,isPersonal,needTech,date):
                self.type = type
                self.isPersonal = isPersonal
                self.needTech = needTech
                self.date = date
                # invoking the __init__ of the parent class 
                Request.__init__(self, name, idnumber) 
class DAO( Request ):
    def __init__(self, name, idnumber,type,isPersonal,needTech):
        self.type = type
        self.isPersonal = isPersonal
        self.needTech = needTech
        Request.__init__(self, name, idnumber)
    rows = [[0 for i in range(5)] for j in range(10)]
    def writeRequest(self):
        filename = "dataBase.csv"
        fields = ['User Name', 'Unique ID', 'Request_type',"Purpose","Need Technician"]
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            DAO.rows[self.idnumber-1][0] = self.name
            DAO.rows[self.idnumber-1][1] = self.idnumber
            DAO.rows[self.idnumber-1][2] = self.type
            DAO.rows[self.idnumber-1][3] = self.isPersonal
            DAO.rows[self.idnumber-1][4] = self.needTech
            print(DAO.rows)
            writer.writerows(DAO.rows)
countUsers = 0
dates = ["1- 11 Tir 12pm to 1pm","2- 12 Tir 14pm to 15pm","3- 14 Tir 7am to 8am"]
while(True):
    print("Do you want to set a request?")
    print("If yes press 1")
    print("other wise 0")
    exit = int(input())
    if(exit == 1):
        print("Hi, What is your Name?")
        countUsers += 1
        name = input()
        user = User(name,countUsers)
        user.say_hi()
        print("Do you want a transportaion Request?")
        print("If yeah press Y")
        request = input()
        if(request == "Y"):
            print("Do you want it for your personal house?")
            print("If yeah press Y")
            request1 = input()
            isPersonal = "Not Personal"
            needTech = "No"
            if(request1 == "Y"):
                isPersonal = "Personal"
                print("Do you need Technician?")
                print("If yeah press Y")
                request = input()
                if(request == "Y"):
                    needTech = "Yes" 
            else:
                needTech = "Yes"
            print(dates)
            print("Which day do you prefer?")
            dayArr = int(input())
            print("Good! Your request has been set.")
            print("See You soon!")
            #Call initialize to make a transportation request instance
            req = Transportation(name,countUsers,"Transportation",isPersonal,needTech,dates[dayArr])
            dao = DAO(name,countUsers,req.type,req.isPersonal,req.needTech)
            dao.writeRequest()
            time.sleep(5)
    else:
        break
