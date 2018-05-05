import pymysql
db= pymysql.connect(host="192.168.87.129",user="root",  
    password="root",db="spider",port=3306)  

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print('Database version :' + str(data))
db.close()