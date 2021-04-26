import mysql.connector
import time

import UI_main

mydb = mysql.connector.connect(
    host="39.106.84.219",  # 数据库主机地址
    user="VLPR",  # 数据库用户名
    passwd="123456",  # 数据库密码
    database="VLPR"
)


def enterStation(results, car_kinds):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM car_info WHERE number = %s"
    val = (str(results),)
    mycursor.execute(sql, val)

    myresult = mycursor.fetchone()  # fetchall() 获取所有记录

    if myresult is not None:
        return myresult
    else:
        a = time.asctime(time.localtime(time.time()))
        mycursor = mydb.cursor()
        id = time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
        sql = "INSERT INTO car_info (id, number, kinds, time) VALUES (%s, %s, %s, %s)"
        val = (int(id), results, car_kinds, a)
        mycursor.execute(sql, val)
        mydb.commit()
        return 0


def Diversion(kinds):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM parkingarea")
    myresult = mycursor.fetchall()
    temp = []
    if kinds == "新能源汽车":
        c = myresult[4][1]
        print(c)
        sql = "UPDATE parkingarea SET counts = %s WHERE areaName = %s"
        val = (int(c) - 1, "E")
        mycursor.execute(sql, val)
        mydb.commit()
        return 'E(新能源专用，含有充电桩)'
    else:
        count = int(0)
        for i in myresult:
            y = (-0.16 * int(i[1]) + 0.4) * float(i[3])
            temp.append(y)
            count = count + 1
    a = temp[0:4]
    max_num = a[0]
    max_index = 0
    for i in range(len(a)):
        if a[i] > max_num:
            max_num = a[i]
            max_index = i
    index = ['A', 'B', 'C', 'D']
    c = myresult[max_index][1]
    sql = "UPDATE parkingarea SET counts = %s WHERE areaName = %s"
    val = (int(c) - 1, index[max_index])
    mycursor.execute(sql, val)
    mydb.commit()
    return index[max_index]


def refreshParking():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM parkingarea")
    myresult = mycursor.fetchall()
    sums = int(0)
    for i in myresult[0:4]:
        sums = sums + int(i[1])

    new = myresult[4][1]
    res = [sums, new]
    return res


def snowflake(area):
    a = time.asctime(time.localtime(time.time()))
    Suffix = time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
    s = ord(area)
    Prefix = bin(s)
    return str(Prefix) + str(Suffix)


def collect(results, car_kinds, times, cost):
    mycursor = mydb.cursor()
    id = snowflake("A")
    sql = "INSERT INTO collect (id, number, kinds, time, cost) VALUES (%s, %s, %s, %s, %s)"
    val = (id, results, car_kinds, times, cost)
    mycursor.execute(sql, val)
    mydb.commit()


def deleteInfo(res):
    mycursor = mydb.cursor()

    sql = "DELETE FROM car_info WHERE number = %s"
    val = (res,)
    mycursor.execute(sql, val)
    mydb.commit()


def billing(kinds, time):
    standard = [0, 0.1, 0.2, 0.3]

    if time <= 3000:
        time = 0
    else:
        time = time / 720

    if kinds == "大型车":
        cost = standard[3] * time
    elif kinds == "新能源汽车":
        cost = standard[1] * time
    elif kinds == "普通车":
        cost = standard[2] * time
    else:
        cost = standard[0] * time
    return cost

def loginSystem(account, password):
    try:
        mycursor = mydb.cursor()
        sql = "SELECT password FROM admin WHERE account = %s"
        na = (str(account), )
        mycursor.execute(sql, na)
        myresult = mycursor.fetchone()
        if myresult[0] == password:
            return 0
        else:
            return 1
    except:
        return 1

def regSystem(account, password):
    try:
        mycursor = mydb.cursor()
        sql = "INSERT INTO admin (account, password) VALUES (%s, %s)"
        val = (account, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return 0
    except:
        return 1