import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import mysql.connector as connector
import datetime
#GRADE 12 INFORMATICS PRACTICES PROJECT
#PROJECT NAME : OLYMPIC DATAMANAGEMENT
#TEAM WORK BY-
#KAMALASH,CHRISTY,MEYYAPPAN
#1923 LINES OF CODE
db=connector.connect(host='localhost',port='3306',user='root',password='balaji-2111',database='olympic_management')
mycursor=db.cursor()
#print("*****OLYMPICS MANAGEMENT SYSTEM*****")
#username=input("Enter your USERNAME: ")
#user="admin"
#if username != user:
#    print(" WRONG USERNAME ENTERED  ")
#elif username==user:
#    print("WELCOME user")
#password = input("Enter your PASSWORD: ")
#passcode = "olympic"
#if password != passcode:
#   print(" WRONG PASSWORD ENTERED  ")
#elif password == passcode:
#    print("  welcome to OLYMPICS MANAGEMENT SYSTEM ")
print("good morning")
while 1:
    print("**************************************************")
    print("1): PARAOLYMPIC")  #table:#DETAILS,DETAILS1,DETAILS2
    print("2): SUMMEROLYMPIC")#table:#DETAILS3,DETAILS4,DETAILS5
    print("3): WINTEROLYMPIC")#table:#DETAILS6,DETAILS7,DETAILS8
    option=input("PLEASE SELECT OPTION FROM ABOVE THREE  : ")
    print("**************************************************")
    if option=="1":
        print("1): Athletics  ")
        print("2): Swimming   ")
        print("3): Archery    ")
        option1=input("PLEASE SELECT ANY OPTION ABOVE THREE  : ")
        print("**************************************************")
        if option1=="1":
            print(" *ATHLETICS* ")#NEED TO MODIFY OPTIONS AT LAST
            print(" 1) ENTER DATA")#PYTHON PART
            print(" 2) SEE DATA")#PANDA PART
            print(" 3) DELETE DATA")#PYTHON PART
            print(" 4) UPDATE RECORD")
            print(" 5) SEE WINNERS")#MYSQL PART
            print(" 6) GRAPH OF MEDALS")#MATPLOTLIB PART
            print(" 7) RETURN")#PYTHON PART
            print("**************************************************")
            option2=input("PLEASE SELECT ANY OPTION ABOVE : ")
            if option2=="1":          
                print("")
                print("1) 100m")
                print("2) 200m")
                print("3) 400m")
                option4=input("PLEASE CHOOSE ANY OPTION ")
                print("**************************************************")
                if option4=="1":
                    print("100m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="2":
                    print("200m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="3":
                    print("400m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
            if option2=="2":
                    print("player details")
                    print("NAME , AGE , COUNTRY , PHONE_NUMBER , RANK , GENDER , METER , TIME , SPORT_NAME , DATE_OF_MEDAL , id ")
                    mycursor.execute("SELECT*FROM Details")
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="3":
                print("DELETE RECORD OF PLAYER ")
                ac=input('ENTER personID TO BE DELTED :')
                st="DELETE  FROM Details WHERE personID='%s'"%(ac)
                mycursor.execute(st)
                db.commit()
                print("DATA DELETED")
                print("**************************************************")
            if option2=="4":
                print("update data ")
                print("1) EDIT PLAYER NAME ")
                print("2) EDIT PLAYER RANK  ")
                print("3) EDIT WIN DATE ")
                print("4) EDIT PLAYER GENDER ")
                print("5) EDIT PLAYER COUNTRY ")
                print("6) EDIT SPORT NAME ")
                print("7) EDIT PLAYER WIN TIME  ")
                print("8) EDIT PLAYER AGE ")
                option4=input("ENTER THE CHOICE ")
                if option4=="1":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT NAME :")
                    st="UPDATE Details SET name='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")

                if option4=="2":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE RANK :")
                    st="UPDATE Details1 SET rank='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="3":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DATE :")
                    st="UPDATE Details1 SET yearmedal='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="4":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE GENDER :")
                    st="UPDATE Details1 SET sex='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="5":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT COUNTRY NAME :")
                    st="UPDATE Details1 SET country='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="6":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT SPORT NAME :")
                    st="UPDATE Details1 SET sportname='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="7":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DURATION :")
                    st="UPDATE Details1 SET time='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="8":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT AGE :")
                    st="UPDATE Details1 SET age='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")

            if option2=="5":
                print(" THE WINNERS ARE ")
                winlist=("SELECT name,yearmedal,rank,sportname,meter,time FROM Details")
                mycursor.execute(winlist)
                results=mycursor.fetchall()
                for row in results:
                    name=row[0]
                    yearmedal=row[1]
                    rank=row[2]
                    sportname=row[3]
                    print("NAME : "+name)
                    print("year of medal : "+yearmedal)
                    print("rank : "+rank)
                    print("sport name : "+sportname)
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="6":
                print("graph of medals")
                print("1) BAR GRAPH OF WINNER AND TIME TAKEN ")
                print("2) SCATTER PLOT OF WINNER AND TIME TAKEN ")
                option3=input("ENTER OPTION : ")
                if option3=="1":
                        mycursor.execute("SELECT name,time FROM Details")
                        result=mycursor.fetchall
                        Name=[]
                        Time=[]
                        for i in mycursor:
                            Name.append(i[0])
                            Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.bar(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")
                if option3=="2":
                    mycursor.execute("SELECT name,time FROM Details")
                    result=mycursor.fetchall
                    Name=[]
                    Time=[]
                    for i in mycursor:
                        Name.append(i[0])
                        Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.scatter(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")                    
                        print("**************************************************")
        
        if option1=="2":
            print(" *SWIMMING* ")#NEED TO MODIFY OPTIONS AT LAST
            print(" 1) ENTER DATA")#PYTHON PART
            print(" 2) SEE DATA")#PANDA PART
            print(" 3) DELETE DATA")#PYTHON PART
            print(" 4) UPDATE RECORD")
            print(" 5) SEE WINNERS")#MYSQL PART
            print(" 6) GRAPH OF MEDALS")#MATPLOTLIB PART
            print(" 7) RETURN")#PYTHON PART
            print("**************************************************")
            option2=input("PLEASE SELECT ANY OPTION ABOVE : ")
            if option2=="1":          
                print("")
                print("1) 100m")
                print("2) 200m")
                print("3) 400m")
                option4=input("PLEASE CHOOSE ANY OPTION ")
                print("**************************************************")
                if option4=="1":
                    print("100m")
                    mycursor=db.cursor()
                    mycursor.execute("CREATE TABLE Details1(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details1(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="2":
                    print("200m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details1(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="3":
                    print("400m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details1(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details1(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
            if option2=="2":
                    print("player details")
                    print("NAME , AGE , COUNTRY , PHONE_NUMBER , RANK , GENDER , METER , TIME , SPORT_NAME , DATE_OF_MEDAL , id ")
                    mycursor.execute("SELECT*FROM Details1")
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="3":
                print("DELETE RECORD OF PLAYER ")
                ac=input('ENTER personID TO BE DELTED :')
                st="DELETE  FROM Details1 WHERE personID='%s'"%(ac)
                mycursor.execute(st)
                db.commit()
                print("DATA DELETED")
                print("**************************************************")
            if option2=="4":
                print("update data ")
                print("1) EDIT PLAYER NAME ")
                print("2) EDIT PLAYER RANK  ")
                print("3) EDIT WIN DATE ")
                print("4) EDIT PLAYER GENDER ")
                print("5) EDIT PLAYER COUNTRY ")
                print("6) EDIT SPORT NAME ")
                print("7) EDIT PLAYER WIN TIME  ")
                print("8) EDIT PLAYER AGE ")
                option4=input("ENTER THE CHOICE ")
                if option4=="1":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT NAME :")
                    st="UPDATE Details1 SET name='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="2":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE RANK :")
                    st="UPDATE Details1 SET rank='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="3":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DATE :")
                    st="UPDATE Details1 SET yearmedal='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="4":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE GENDER :")
                    st="UPDATE Details1 SET sex='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="5":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT COUNTRY NAME :")
                    st="UPDATE Details1 SET country='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="6":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT SPORT NAME :")
                    st="UPDATE Details1 SET sportname='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="7":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DURATION :")
                    st="UPDATE Details1 SET time='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="8":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT AGE :")
                    st="UPDATE Details1 SET age='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
            if option2=="5":
                print(" THE WINNERS ARE ")
                winlist=("SELECT name,yearmedal,rank,sportname,meter,time FROM Details1")
                mycursor.execute(winlist)
                results=mycursor.fetchall()
                for row in results:
                    name=row[0]
                    yearmedal=row[1]
                    rank=row[2]
                    sportname=row[3]
                    print("NAME : "+name)
                    print("year of medal : "+yearmedal)
                    print("rank : "+rank)
                    print("sport name : "+sportname)
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="6":
                print("graph of medals")
                print("1) BAR GRAPH OF WINNER AND TIME TAKEN ")
                print("2) SCATTER PLOT OF WINNER AND TIME TAKEN ")
                option3=input("ENTER OPTION : ")
                if option3=="1":
                        mycursor.execute("SELECT name,time FROM Details1")
                        result=mycursor.fetchall
                        Name=[]
                        Time=[]
                        for i in mycursor:
                            Name.append(i[0])
                            Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.bar(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")
                if option3=="2":
                    mycursor.execute("SELECT name,time FROM Details1")
                    result=mycursor.fetchall
                    Name=[]
                    Time=[]
                    for i in mycursor:
                        Name.append(i[0])
                        Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.scatter(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")                    
                        print("**************************************************")

        if option1=="3":
            
            print(" *ARCHERY* ")#NEED TO MODIFY OPTIONS AT LAST
            print(" 1) ENTER DATA")#PYTHON PART
            print(" 2) SEE DATA")#PANDA PART
            print(" 3) DELETE DATA")#PYTHON PART
            print(" 4) UPDATE RECORD")
            print(" 5) SEE WINNERS")#MYSQL PART
            print(" 6) GRAPH OF MEDALS")#MATPLOTLIB PART
            print(" 7) RETURN")#PYTHON PART
            print("**************************************************")
            option2=input("PLEASE SELECT ANY OPTION ABOVE : ")
            if option2=="1":          
                print("")
                print("1) 100m")
                print("2) 200m")
                print("3) 400m")
                option4=input("PLEASE CHOOSE ANY OPTION ")
                print("**************************************************")
                if option4=="1":
                    print("100m")
                    mycursor=db.cursor()
                    mycursor.execute("CREATE TABLE Details2(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details2(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="2":
                    print("200m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details2(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details2(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="3":
                    print("400m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details2(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details2(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
            if option2=="2":
                    print("player details")
                    print("NAME , AGE , COUNTRY , PHONE_NUMBER , RANK , GENDER , METER , TIME , SPORT_NAME , DATE_OF_MEDAL , id ")
                    mycursor.execute("SELECT*FROM Details2")
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="3":
                print("DELETE RECORD OF PLAYER ")
                ac=input('ENTER personID TO BE DELTED :')
                st="DELETE  FROM Details2 WHERE personID='%s'"%(ac)
                mycursor.execute(st)
                db.commit()
                print("DATA DELETED")
                print("**************************************************")
            if option2=="4":
                print("update data ")
                print("1) EDIT PLAYER NAME ")
                print("2) EDIT PLAYER RANK  ")
                print("3) EDIT WIN DATE ")
                print("4) EDIT PLAYER GENDER ")
                print("5) EDIT PLAYER COUNTRY ")
                print("6) EDIT SPORT NAME ")
                print("7) EDIT PLAYER WIN TIME  ")
                print("8) EDIT PLAYER AGE ")
                option4=input("ENTER THE CHOICE ")
                if option4=="1":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT NAME :")
                    st="UPDATE Details2 SET name='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="2":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE RANK :")
                    st="UPDATE Details2 SET rank='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="3":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DATE :")
                    st="UPDATE Details2 SET yearmedal='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="4":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE GENDER :")
                    st="UPDATE Details2 SET sex='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="5":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT COUNTRY NAME :")
                    st="UPDATE Details2 SET country='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="6":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT SPORT NAME :")
                    st="UPDATE Details2 SET sportname='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="7":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DURATION :")
                    st="UPDATE Details2 SET time='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="8":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT AGE :")
                    st="UPDATE Details2 SET age='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
            if option2=="5":
                print(" THE WINNERS ARE ")
                winlist=("SELECT name,yearmedal,rank,sportname,meter,time FROM Details2")
                mycursor.execute(winlist)
                results=mycursor.fetchall()
                for row in results:
                    name=row[0]
                    yearmedal=row[1]
                    rank=row[2]
                    sportname=row[3]
                    print("NAME : "+name)
                    print("year of medal : "+yearmedal)
                    print("rank : "+rank)
                    print("sport name : "+sportname)
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="6":
                print("graph of medals")
                print("1) BAR GRAPH OF WINNER AND TIME TAKEN ")
                print("2) SCATTER PLOT OF WINNER AND TIME TAKEN ")
                option3=input("ENTER OPTION : ")
                if option3=="1":
                        mycursor.execute("SELECT name,time FROM Details2")
                        result=mycursor.fetchall
                        Name=[]
                        Time=[]
                        for i in mycursor:
                            Name.append(i[0])
                            Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.bar(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")
                if option3=="2":
                    mycursor.execute("SELECT name,time FROM Details2")
                    result=mycursor.fetchall
                    Name=[]
                    Time=[]
                    for i in mycursor:
                        Name.append(i[0])
                        Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.scatter(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")                    
                        print("**************************************************")
    if option=="2":
        print("SUMMER OLYMPICS")
        print("1): Cycling  ")
        print("2): Triathlon   ")
        print("3): Archery    ")
        option1=input("PLEASE SELECT ANY OPTION ABOVE THREE  : ")
        print("**************************************************")
        if option1=="1":
            print(" *ATHLETICS* ")#NEED TO MODIFY OPTIONS AT LAST
            print(" 1) ENTER DATA")#PYTHON PART
            print(" 2) SEE DATA")#PANDA PART
            print(" 3) DELETE DATA")#PYTHON PART
            print(" 4) UPDATE RECORD")
            print(" 5) SEE WINNERS")#MYSQL PART
            print(" 6) GRAPH OF MEDALS")#MATPLOTLIB PART
            print(" 7) RETURN")#PYTHON PART
            print("**************************************************")
            option2=input("PLEASE SELECT ANY OPTION ABOVE : ")
            if option2=="1":          
                print("")
                print("1) 100m")
                print("2) 200m")
                print("3) 400m")
                option4=input("PLEASE CHOOSE ANY OPTION ")
                print("**************************************************")
                if option4=="1":
                    print("100m")
                    mycursor=db.cursor()
                    mycursor.execute("CREATE TABLE Details3(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details3(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="2":
                    print("200m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details3(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details3(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="3":
                    print("400m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details3(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details3(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
            if option2=="2":
                    print("player details")
                    print("NAME , AGE , COUNTRY , PHONE_NUMBER , RANK , GENDER , METER , TIME , SPORT_NAME , DATE_OF_MEDAL , id ")
                    mycursor.execute("SELECT*FROM Details3")
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="3":
                print("DELETE RECORD OF PLAYER ")
                ac=input('ENTER personID TO BE DELTED :')
                st="DELETE  FROM Details3 WHERE personID='%s'"%(ac)
                mycursor.execute(st)
                db.commit()
                print("DATA DELETED")
                print("**************************************************")
            if option2=="4":
                print("update data ")
                print("1) EDIT PLAYER NAME ")
                print("1) EDIT PLAYER RANK  ")
                print("1) EDIT WIN DATE ")
                print("1) EDIT PLAYER GENDER ")
                print("1) EDIT PLAYER COUNTRY ")
                print("1) EDIT SPORT NAME ")
                print("1) EDIT PLAYER WIN TIME  ")
                print("1) EDIT PLAYER AGE ")
                option4=input("ENTER THE CHOICE ")
                if option4=="1":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT NAME :")
                    st="UPDATE Details3 SET name='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="2":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE RANK :")
                    st="UPDATE Details3 SET rank='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="3":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DATE :")
                    st="UPDATE Details3 SET yearmedal='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="4":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE GENDER :")
                    st="UPDATE Details3 SET sex='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="5":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT COUNTRY NAME :")
                    st="UPDATE Details3 SET country='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="6":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT SPORT NAME :")
                    st="UPDATE Details3 SET sportname='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="7":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DURATION :")
                    st="UPDATE Details3 SET time='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="8":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT AGE :")
                    st="UPDATE Details3 SET age='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
 
            if option2=="5":
                print(" THE WINNERS ARE ")
                winlist=("SELECT name,yearmedal,rank,sportname,meter,time FROM Details3")
                mycursor.execute(winlist)
                results=mycursor.fetchall()
                for row in results:
                    name=row[0]
                    yearmedal=row[1]
                    rank=row[2]
                    sportname=row[3]
                    print("NAME : "+name)
                    print("year of medal : "+yearmedal)
                    print("rank : "+rank)
                    print("sport name : "+sportname)
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="6":
                print("graph of medals")
                print("1) BAR GRAPH OF WINNER AND TIME TAKEN ")
                print("2) SCATTER PLOT OF WINNER AND TIME TAKEN ")
                option3=input("ENTER OPTION : ")
                if option3=="1":
                        mycursor.execute("SELECT name,time FROM Details3")
                        result=mycursor.fetchall
                        Name=[]
                        Time=[]
                        for i in mycursor:
                            Name.append(i[0])
                            Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.bar(Name,Time,color=['r','b'])
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")
                if option3=="2":
                    mycursor.execute("SELECT name,time FROM Details3")
                    result=mycursor.fetchall
                    Name=[]
                    Time=[]
                    for i in mycursor:
                        Name.append(i[0])
                        Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.scatter(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")                    
                        print("**************************************************")
        
        if option1=="2":
            print(" *SWIMMING* ")#NEED TO MODIFY OPTIONS AT LAST
            print(" 1) ENTER DATA")#PYTHON PART
            print(" 2) SEE DATA")#PANDA PART
            print(" 3) DELETE DATA")#PYTHON PART
            print(" 4) UPDATE RECORD")
            print(" 5) SEE WINNERS")#MYSQL PART
            print(" 6) GRAPH OF MEDALS")#MATPLOTLIB PART
            print(" 7) RETURN")#PYTHON PART
            print("**************************************************")
            option2=input("PLEASE SELECT ANY OPTION ABOVE : ")
            if option2=="1":          
                print("")
                print("1) 100m")
                print("2) 200m")
                print("3) 400m")
                option4=input("PLEASE CHOOSE ANY OPTION ")
                print("**************************************************")
                if option4=="1":
                    print("100m")
                    mycursor=db.cursor()
                    mycursor.execute("CREATE TABLE Details4(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details4(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="2":
                    print("200m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details4(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details4(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="3":
                    print("400m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details4(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details4(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
            if option2=="2":
                    print("player details")
                    print("NAME , AGE , COUNTRY , PHONE_NUMBER , RANK , GENDER , METER , TIME , SPORT_NAME , DATE_OF_MEDAL , id ")
                    mycursor.execute("SELECT*FROM Details4")
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="3":
                print("DELETE RECORD OF PLAYER ")
                ac=input('ENTER personID TO BE DELTED :')
                st="DELETE  FROM Details4 WHERE personID='%s'"%(ac)
                mycursor.execute(st)
                db.commit()
                print("DATA DELETED")
                print("**************************************************")
            if option2=="4":
                print("update data ")
                print("1) EDIT PLAYER NAME ")
                print("2) EDIT PLAYER RANK  ")
                print("3) EDIT WIN DATE ")
                print("4) EDIT PLAYER GENDER ")
                print("5) EDIT PLAYER COUNTRY ")
                print("6) EDIT SPORT NAME ")
                print("7) EDIT PLAYER WIN TIME  ")
                print("8) EDIT PLAYER AGE ")
                option4=input("ENTER THE CHOICE ")
                if option4=="1":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT NAME :")
                    st="UPDATE Details4 SET name='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="2":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE RANK :")
                    st="UPDATE Details4 SET rank='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="3":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DATE :")
                    st="UPDATE Details4 SET yearmedal='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="4":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE GENDER :")
                    st="UPDATE Details4 SET sex='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="5":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT COUNTRY NAME :")
                    st="UPDATE Details4 SET country='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="6":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT SPORT NAME :")
                    st="UPDATE Details4 SET sportname='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="7":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DURATION :")
                    st="UPDATE Details4 SET time='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="8":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT AGE :")
                    st="UPDATE Details4 SET age='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
            if option2=="5":
                print(" THE WINNERS ARE ")
                winlist=("SELECT name,yearmedal,rank,sportname,meter,time FROM Details4")
                mycursor.execute(winlist)
                results=mycursor.fetchall()
                for row in results:
                    name=row[0]
                    yearmedal=row[1]
                    rank=row[2]
                    sportname=row[3]
                    print("NAME : "+name)
                    print("year of medal : "+yearmedal)
                    print("rank : "+rank)
                    print("sport name : "+sportname)
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="6":
                print("graph of medals")
                print("1) BAR GRAPH OF WINNER AND TIME TAKEN ")
                print("2) SCATTER PLOT OF WINNER AND TIME TAKEN ")
                option3=input("ENTER OPTION : ")
                if option3=="1":
                        mycursor.execute("SELECT name,time FROM Details4")
                        result=mycursor.fetchall
                        Name=[]
                        Time=[]
                        for i in mycursor:
                            Name.append(i[0])
                            Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.bar(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")
                if option3=="2":
                    mycursor.execute("SELECT name,time FROM Details4")
                    result=mycursor.fetchall
                    Name=[]
                    Time=[]
                    for i in mycursor:
                        Name.append(i[0])
                        Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.scatter(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")                    
                        print("**************************************************")

        if option1=="3":
            
            print(" *ARCHERY* ")#NEED TO MODIFY OPTIONS AT LAST
            print(" 1) ENTER DATA")#PYTHON PART
            print(" 2) SEE DATA")#PANDA PART
            print(" 3) DELETE DATA")#PYTHON PART
            print(" 4) UPDATE RECORD")
            print(" 5) SEE WINNERS")#MYSQL PART
            print(" 6) GRAPH OF MEDALS")#MATPLOTLIB PART
            print(" 7) RETURN")#PYTHON PART
            print("**************************************************")
            option2=input("PLEASE SELECT ANY OPTION ABOVE : ")
            if option2=="1":          
                print("")
                print("1) 100m")
                print("2) 200m")
                print("3) 400m")
                option4=input("PLEASE CHOOSE ANY OPTION ")
                print("**************************************************")
                if option4=="1":
                    print("100m")
                    mycursor=db.cursor()
                    mycursor.execute("CREATE TABLE Details5(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details5(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="2":
                    print("200m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details5(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details5(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="3":
                    print("400m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details5(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details5(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
            if option2=="2":
                    print("player details")
                    print("NAME , AGE , COUNTRY , PHONE_NUMBER , RANK , GENDER , METER , TIME , SPORT_NAME , DATE_OF_MEDAL , id ")
                    mycursor.execute("SELECT*FROM Details5")
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="3":
                print("DELETE RECORD OF PLAYER ")
                ac=input('ENTER personID TO BE DELTED :')
                st="DELETE  FROM Details5 WHERE personID='%s'"%(ac)
                mycursor.execute(st)
                db.commit()
                print("DATA DELETED")
                print("**************************************************")
            if option2=="4":
                print("update data ")
                print("1) EDIT PLAYER NAME ")
                print("2) EDIT PLAYER RANK  ")
                print("3) EDIT WIN DATE ")
                print("4) EDIT PLAYER GENDER ")
                print("5) EDIT PLAYER COUNTRY ")
                print("6) EDIT SPORT NAME ")
                print("7) EDIT PLAYER WIN TIME  ")
                print("8) EDIT PLAYER AGE ")
                option4=input("ENTER THE CHOICE ")
                if option4=="1":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT NAME :")
                    st="UPDATE Details5 SET name='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="2":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE RANK :")
                    st="UPDATE Details5 SET rank='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="3":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DATE :")
                    st="UPDATE Details5 SET yearmedal='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="4":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE GENDER :")
                    st="UPDATE Details5 SET sex='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="5":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT COUNTRY NAME :")
                    st="UPDATE Details5 SET country='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="6":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT SPORT NAME :")
                    st="UPDATE Details5 SET sportname='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="7":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DURATION :")
                    st="UPDATE Details2 SET time='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="8":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT AGE :")
                    st="UPDATE Details5 SET age='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
            if option2=="5":
                print(" THE WINNERS ARE ")
                winlist=("SELECT name,yearmedal,rank,sportname,meter,time FROM Details5")
                mycursor.execute(winlist)
                results=mycursor.fetchall()
                for row in results:
                    name=row[0]
                    yearmedal=row[1]
                    rank=row[2]
                    sportname=row[3]
                    print("NAME : "+name)
                    print("year of medal : "+yearmedal)
                    print("rank : "+rank)
                    print("sport name : "+sportname)
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="6":
                print("graph of medals")
                print("1) BAR GRAPH OF WINNER AND TIME TAKEN ")
                print("2) SCATTER PLOT OF WINNER AND TIME TAKEN ")
                option3=input("ENTER OPTION : ")
                if option3=="1":
                        mycursor.execute("SELECT name,time FROM Details5")
                        result=mycursor.fetchall
                        Name=[]
                        Time=[]
                        for i in mycursor:
                            Name.append(i[0])
                            Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.bar(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")
                if option3=="2":
                    mycursor.execute("SELECT name,time FROM Details5")
                    result=mycursor.fetchall
                    Name=[]
                    Time=[]
                    for i in mycursor:
                        Name.append(i[0])
                        Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.scatter(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")                    
                        print("**************************************************")
    if option=="3":
        print("WINTER OLYMPICS")
        print("1): Athletics  ")
        print("2): Swimming   ")
        print("3): Archery    ")
        option1=input("PLEASE SELECT ANY OPTION ABOVE THREE  : ")
        print("**************************************************")
        if option1=="1":
            print(" *ATHLETICS* ")#NEED TO MODIFY OPTIONS AT LAST
            print(" 1) ENTER DATA")#PYTHON PART
            print(" 2) SEE DATA")#PANDA PART
            print(" 3) DELETE DATA")#PYTHON PART
            print(" 4) UPDATE RECORD")
            print(" 5) SEE WINNERS")#MYSQL PART
            print(" 6) GRAPH OF MEDALS")#MATPLOTLIB PART
            print(" 7) RETURN")#PYTHON PART
            print("**************************************************")
            option2=input("PLEASE SELECT ANY OPTION ABOVE : ")
            if option2=="1":          
                print("")
                print("1) 100m")
                print("2) 200m")
                print("3) 400m")
                option4=input("PLEASE CHOOSE ANY OPTION ")
                print("**************************************************")
                if option4=="1":
                    print("100m")
                    mycursor=db.cursor()
                    mycursor.execute("CREATE TABLE Details6(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details6(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="2":
                    print("200m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details6(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details6(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="3":
                    print("400m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details6(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details6(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
            if option2=="2":
                    print("player details")
                    print("NAME , AGE , COUNTRY , PHONE_NUMBER , RANK , GENDER , METER , TIME , SPORT_NAME , DATE_OF_MEDAL , id ")
                    mycursor.execute("SELECT*FROM Details3")
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="3":
                print("DELETE RECORD OF PLAYER ")
                ac=input('ENTER personID TO BE DELTED :')
                st="DELETE  FROM Details6 WHERE personID='%s'"%(ac)
                mycursor.execute(st)
                db.commit()
                print("DATA DELETED")
                print("**************************************************")
            if option2=="4":
                print("update data ")
                print("1) EDIT PLAYER NAME ")
                print("1) EDIT PLAYER RANK  ")
                print("1) EDIT WIN DATE ")
                print("1) EDIT PLAYER GENDER ")
                print("1) EDIT PLAYER COUNTRY ")
                print("1) EDIT SPORT NAME ")
                print("1) EDIT PLAYER WIN TIME  ")
                print("1) EDIT PLAYER AGE ")
                option4=input("ENTER THE CHOICE ")
                if option4=="1":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT NAME :")
                    st="UPDATE Details6 SET name='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="2":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE RANK :")
                    st="UPDATE Details6 SET rank='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="3":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DATE :")
                    st="UPDATE Details6 SET yearmedal='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="4":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE GENDER :")
                    st="UPDATE Details6 SET sex='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="5":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT COUNTRY NAME :")
                    st="UPDATE Details6 SET country='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="6":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT SPORT NAME :")
                    st="UPDATE Details6 SET sportname='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="7":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DURATION :")
                    st="UPDATE Details6 SET time='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="8":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT AGE :")
                    st="UPDATE Details6 SET age='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
 
            if option2=="5":
                print(" THE WINNERS ARE ")
                winlist=("SELECT name,yearmedal,rank,sportname,meter,time FROM Details6")
                mycursor.execute(winlist)
                results=mycursor.fetchall()
                for row in results:
                    name=row[0]
                    yearmedal=row[1]
                    rank=row[2]
                    sportname=row[3]
                    print("NAME : "+name)
                    print("year of medal : "+yearmedal)
                    print("rank : "+rank)
                    print("sport name : "+sportname)
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="6":
                print("graph of medals")
                print("1) BAR GRAPH OF WINNER AND TIME TAKEN ")
                print("2) SCATTER PLOT OF WINNER AND TIME TAKEN ")
                option3=input("ENTER OPTION : ")
                if option3=="1":
                        mycursor.execute("SELECT name,time FROM Details6")
                        result=mycursor.fetchall
                        Name=[]
                        Time=[]
                        for i in mycursor:
                            Name.append(i[0])
                            Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.bar(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")
                if option3=="2":
                    mycursor.execute("SELECT name,time FROM Details6")
                    result=mycursor.fetchall
                    Name=[]
                    Time=[]
                    for i in mycursor:
                        Name.append(i[0])
                        Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.scatter(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")                    
                        print("**************************************************")
        
        if option1=="2":
            print(" *SWIMMING* ")#NEED TO MODIFY OPTIONS AT LAST
            print(" 1) ENTER DATA")#PYTHON PART
            print(" 2) SEE DATA")#PANDA PART
            print(" 3) DELETE DATA")#PYTHON PART
            print(" 4) UPDATE RECORD")
            print(" 5) SEE WINNERS")#MYSQL PART
            print(" 6) GRAPH OF MEDALS")#MATPLOTLIB PART
            print(" 7) RETURN")#PYTHON PART
            print("**************************************************")
            option2=input("PLEASE SELECT ANY OPTION ABOVE : ")
            if option2=="1":          
                print("")
                print("1) 100m")
                print("2) 200m")
                print("3) 400m")
                option4=input("PLEASE CHOOSE ANY OPTION ")
                print("**************************************************")
                if option4=="1":
                    print("100m")
                    mycursor=db.cursor()
                    mycursor.execute("CREATE TABLE Details7(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details7(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="2":
                    print("200m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details7(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details7(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="3":
                    print("400m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details7(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details7(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
            if option2=="2":
                    print("player details")
                    print("NAME , AGE , COUNTRY , PHONE_NUMBER , RANK , GENDER , METER , TIME , SPORT_NAME , DATE_OF_MEDAL , id ")
                    mycursor.execute("SELECT*FROM Details7")
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="3":
                print("DELETE RECORD OF PLAYER ")
                ac=input('ENTER personID TO BE DELTED :')
                st="DELETE  FROM Details7 WHERE personID='%s'"%(ac)
                mycursor.execute(st)
                db.commit()
                print("DATA DELETED")
                print("**************************************************")
            if option2=="4":
                print("update data ")
                print("1) EDIT PLAYER NAME ")
                print("2) EDIT PLAYER RANK  ")
                print("3) EDIT WIN DATE ")
                print("4) EDIT PLAYER GENDER ")
                print("5) EDIT PLAYER COUNTRY ")
                print("6) EDIT SPORT NAME ")
                print("7) EDIT PLAYER WIN TIME  ")
                print("8) EDIT PLAYER AGE ")
                option4=input("ENTER THE CHOICE ")
                if option4=="1":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT NAME :")
                    st="UPDATE Details7 SET name='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="2":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE RANK :")
                    st="UPDATE Details7 SET rank='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="3":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DATE :")
                    st="UPDATE Details7 SET yearmedal='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="4":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE GENDER :")
                    st="UPDATE Details7 SET sex='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="5":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT COUNTRY NAME :")
                    st="UPDATE Details7 SET country='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="6":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT SPORT NAME :")
                    st="UPDATE Details7 SET sportname='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="7":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DURATION :")
                    st="UPDATE Details7 SET time='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="8":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT AGE :")
                    st="UPDATE Details7 SET age='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
            if option2=="5":
                print(" THE WINNERS ARE ")
                winlist=("SELECT name,yearmedal,rank,sportname,meter,time FROM Details7")
                mycursor.execute(winlist)
                results=mycursor.fetchall()
                for row in results:
                    name=row[0]
                    yearmedal=row[1]
                    rank=row[2]
                    sportname=row[3]
                    print("NAME : "+name)
                    print("year of medal : "+yearmedal)
                    print("rank : "+rank)
                    print("sport name : "+sportname)
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="6":
                print("graph of medals")
                print("1) BAR GRAPH OF WINNER AND TIME TAKEN ")
                print("2) SCATTER PLOT OF WINNER AND TIME TAKEN ")
                option3=input("ENTER OPTION : ")
                if option3=="1":
                        mycursor.execute("SELECT name,time FROM Details7")
                        result=mycursor.fetchall
                        Name=[]
                        Time=[]
                        for i in mycursor:
                            Name.append(i[0])
                            Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.bar(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")
                if option3=="2":
                    mycursor.execute("SELECT name,time FROM Details7")
                    result=mycursor.fetchall
                    Name=[]
                    Time=[]
                    for i in mycursor:
                        Name.append(i[0])
                        Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.scatter(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")                    
                        print("**************************************************")

        if option1=="3":
            
            print(" *ARCHERY* ")#NEED TO MODIFY OPTIONS AT LAST
            print(" 1) ENTER DATA")#PYTHON PART
            print(" 2) SEE DATA")#PANDA PART
            print(" 3) DELETE DATA")#PYTHON PART
            print(" 4) UPDATE RECORD")
            print(" 5) SEE WINNERS")#MYSQL PART
            print(" 6) GRAPH OF MEDALS")#MATPLOTLIB PART
            print(" 7) RETURN")#PYTHON PART
            print("**************************************************")
            option2=input("PLEASE SELECT ANY OPTION ABOVE : ")
            if option2=="1":          
                print("")
                print("1) 100m")
                print("2) 200m")
                print("3) 400m")
                option4=input("PLEASE CHOOSE ANY OPTION ")
                print("**************************************************")
                if option4=="1":
                    print("100m")
                    mycursor=db.cursor()
                    mycursor.execute("CREATE TABLE Details8(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details8(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="2":
                    print("200m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details8(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details8(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
                if option4=="3":
                    print("400m")
                    mycursor=db.cursor()
                    #mycursor.execute("CREATE TABLE Details8(name VARCHAR(50),age VARCHAR(2),country VARCHAR(50),phone VARCHAR(12),rank VARCHAR(25),sex VARCHAR(1),meter int(4),time int(5),sportname VARCHAR(15),yearmedal VARCHAR(14),personID int PRIMARY KEY AUTO_INCREMENT)")
                    name=input("PLEASE ENTER YOUR NAME : ")
                    age=input("PLEASE ENTER YOUR AGE : ")
                    country=input("PLEASE ENTER YOUR COUNTRY : ")
                    phone=input("PLEASE ENTER YOUR PHONE : ")
                    rank=input("PLEASE ENTER YOUR RANK (GOLD/SILVER/BRONZE) : ")
                    sex=input("PLEASE ENTER YOUR SEX(M/F) : ")
                    meter=input("PLEASE ENTER THE DISTANCE(100M/200M/400M) : ")
                    time=input("PLEASE ENTER THE TIME FINISHED THE RACE IN SECONDS : ")
                    sportname=input("PLEASE ENTER THE SPORT NAME : ")
                    yearmedal=input("PLEASE ENTER THE DATE : ")
                    val=(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal)
                    mycursor.execute("INSERT INTO Details8(name,age,country,phone,rank,sex,meter,time,sportname,yearmedal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val))
                    db.commit()
                    print("ADDED SUCCESFULLY ")
                    print("**************************************************")
            if option2=="2":
                    print("player details")
                    print("NAME , AGE , COUNTRY , PHONE_NUMBER , RANK , GENDER , METER , TIME , SPORT_NAME , DATE_OF_MEDAL , id ")
                    mycursor.execute("SELECT*FROM Details8")
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="3":
                print("DELETE RECORD OF PLAYER ")
                ac=input('ENTER personID TO BE DELTED :')
                st="DELETE  FROM Details8 WHERE personID='%s'"%(ac)
                mycursor.execute(st)
                db.commit()
                print("DATA DELETED")
                print("**************************************************")
            if option2=="4":
                print("update data ")
                print("1) EDIT PLAYER NAME ")
                print("2) EDIT PLAYER RANK  ")
                print("3) EDIT WIN DATE ")
                print("4) EDIT PLAYER GENDER ")
                print("5) EDIT PLAYER COUNTRY ")
                print("6) EDIT SPORT NAME ")
                print("7) EDIT PLAYER WIN TIME  ")
                print("8) EDIT PLAYER AGE ")
                option4=input("ENTER THE CHOICE ")
                if option4=="1":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT NAME :")
                    st="UPDATE Details8 SET name='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="2":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE RANK :")
                    st="UPDATE Details8 SET rank='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="3":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DATE :")
                    st="UPDATE Details8 SET yearmedal='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="4":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE GENDER :")
                    st="UPDATE Details8 SET sex='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="5":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT COUNTRY NAME :")
                    st="UPDATE Details8 SET country='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="6":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT SPORT NAME :")
                    st="UPDATE Details8 SET sportname='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="7":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT DURATION :")
                    st="UPDATE Details8 SET time='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
                if option4=="8":
                    ac=input("ENTER THE PERSON ID :")
                    nm=input("ENTER THE CORRECT AGE :")
                    st="UPDATE Details8 SET age='%s' WHERE personID='%s'"%(nm,ac)
                    mycursor.execute(st)
                    db.commit()
                    print("succeseful ")
            if option2=="5":
                print(" THE WINNERS ARE ")
                winlist=("SELECT name,yearmedal,rank,sportname,meter,time FROM Details8")
                mycursor.execute(winlist)
                results=mycursor.fetchall()
                for row in results:
                    name=row[0]
                    yearmedal=row[1]
                    rank=row[2]
                    sportname=row[3]
                    print("NAME : "+name)
                    print("year of medal : "+yearmedal)
                    print("rank : "+rank)
                    print("sport name : "+sportname)
                    for x in mycursor:
                        print(x)
                    print("**************************************************")
            if option2=="6":
                print("graph of medals")
                print("1) BAR GRAPH OF WINNER AND TIME TAKEN ")
                print("2) SCATTER PLOT OF WINNER AND TIME TAKEN ")
                option3=input("ENTER OPTION : ")
                if option3=="1":
                        mycursor.execute("SELECT name,time FROM Details8")
                        result=mycursor.fetchall
                        Name=[]
                        Time=[]
                        for i in mycursor:
                            Name.append(i[0])
                            Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.bar(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")
                if option3=="2":
                    mycursor.execute("SELECT name,time FROM Details8")
                    result=mycursor.fetchall
                    Name=[]
                    Time=[]
                    for i in mycursor:
                        Name.append(i[0])
                        Time.append(i[1])
                        print("THE NAME : ",Name)
                        print("THE TIME FOR COMPLETING THE RACE : ",Time)
                        plt.scatter(Name,Time)
                        plt.xlabel("name of player ")
                        plt.ylabel("time taken to finish the race ")
                        plt.title("TIME TAKEN TO COMPLETE THE RACE")
                        plt.show()
                        print("**************************************************")                    
                        print("**************************************************")


    
    
