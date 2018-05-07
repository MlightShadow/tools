import pymysql
db= pymysql.connect(host="192.168.87.129",user="root",  
    password="root",db="spider",port=3306, charset='utf8')  

insert_template = ''
insert_data = []


def sqlMaker(template, data):
    return ''

def executeSQL(cursor, sql):
    res = 0
    try:
        res = cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        res = -1
    return res


cursor = db.cursor()
executeSQL(cursor, sqlMakers(insert_template, insert_data))


#cursor.execute("SELECT VERSION()")
#data = cursor.fetchone()
#print('Database version :' + str(data))
db.close()