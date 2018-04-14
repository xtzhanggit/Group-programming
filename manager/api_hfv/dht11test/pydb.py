import pymysql

def db_get(sql,database): 
    db = pymysql.connect(host = "127.0.0.1", port = 12306 ,user = "root", passwd = "Vudo3423",db = database)
    cursor = db.cursor()
    cursor.execute(sql)
    cur_result = cursor.fetchall()
    cursor.close()
    db.close()
    return cur_result

def db_exe(sql,database):
    db = pymysql.connect(host = "127.0.0.1", port = 12306, user = "root", passwd = "Vudo3423", db = database)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

