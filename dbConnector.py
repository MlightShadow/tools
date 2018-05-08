import pymysql

def insertJobInfo(cursor, data):
    insert_template = '''insert into tb_pos (compName, posTitle, posName, posArea, posAddress, posWelfare, posConditionLabel, posConditionDetail, posCompDetail, url) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
    compName = insert_data.get('compName')
    posTitle = insert_data.get('posTitle')
    posName = insert_data.get('posName')
    posArea = insert_data.get('posArea')
    posAddress = insert_data.get('posAddress')
    posWelfare = insert_data.get('posWelfare')
    posConditionLabel = insert_data.get('posConditionLabel')
    posConditionDetail = insert_data.get('posConditionDetail')
    posCompDetail = insert_data.get('posCompDetail')
    url = insert_data.get('url')
    return cursor.execute(insert_template, (compName, posTitle, posName, posArea, posAddress, posWelfare, posConditionLabel, posConditionDetail, posCompDetail, url))

def executeSQL(data):
    db= pymysql.connect(host="192.168.87.129", user="root", password="root", db="spider", port=3306, charset='utf8')
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


if __name__ == '__main__':
    insert_data = {'compName' : 'compName','posTitle' : 'posTitle','posName' : 'posName','posArea' : 'posArea','posAddress' : 'posAddress','posWelfare' : 'posWelfare','posConditionLabel' : 'posConditionLabel','posConditionDetail' : 'posConditionDetail','posCompDetail' : 'posCompDetail','url' : 'url'}
    executeSQL(insert_data)


#cursor.execute("SELECT VERSION()")
#data = cursor.fetchone()
#print('Database version :' + str(data))
