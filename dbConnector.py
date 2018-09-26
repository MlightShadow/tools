# -*- coding: utf-8 -*-
import pymysql

def insertJobInfo(cursor, data):
    insert_template = '''insert into tb_pos (compName, posTitle, posName, posAddress, posSalary, posWelfare, posConditionLabel, posConditionDetail, posCompDetail, url) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
    compName = data.get('compName')
    posTitle = data.get('posTitle')
    posName = data.get('posName')
    posAddress = data.get('posAddress')
    posSalary = data.get('posSalary')
    posWelfare = data.get('posWelfare')
    posConditionLabel = data.get('posConditionLabel')
    posConditionDetail = data.get('posConditionDetail')
    posCompDetail = data.get('posCompDetail')
    url = data.get('url')
    return cursor.execute(insert_template, (compName, posTitle, posName, posAddress, posSalary, posWelfare, posConditionLabel, posConditionDetail, posCompDetail, url))

def executeSQL(data):
    db= pymysql.connect(host="192.168.87.129", user="root", password="root", db="spider2", port=3306, charset='utf8')
    cursor = db.cursor()
    res = 0
    try:
        res = insertJobInfo(cursor, data)
        db.commit()
    except Exception as e:
        db.rollback()
        res = -1
        print(repr(e))
    
    print('执行成功: 共计'+ str(res) + '条')
    db.close()

def getInfo():
    db= pymysql.connect(host="192.168.87.129", user="root", password="root", db="spider2", port=3306, charset='utf8')
    cursor = db.cursor()
    list = []
    try:
        insert_template = '''select posConditionDetail, posConditionLabel from tb_pos'''
        cursor.execute(insert_template)
        results = cursor.fetchall()
        for row in results:
            list.append(row[0])
            list.append(row[1])
    except Exception as e:
        list = []
        print(repr(e))

    db.close()
    return list


if __name__ == '__main__':
    #insert_data = {'compName' : 'compName','posTitle' : 'posTitle','posName' : 'posName','posAddress' : 'posAddress','posSalary' : 'posSalary','posWelfare' : 'posWelfare','posConditionLabel' : 'posConditionLabel','posConditionDetail' : 'posConditionDetail','posCompDetail' : 'posCompDetail','url' : 'url'}
    #executeSQL(insert_data)
    print(getInfo())


#cursor.execute("SELECT VERSION()")
#data = cursor.fetchone()
#print('Database version :' + str(data))
