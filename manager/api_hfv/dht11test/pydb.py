import pymysql

def db_get(sql): 
    db = pymysql.connect("mysql_test", "root", "Vudo3423", "HiDockerwifi")
    cursor = db.cursor()
    cursor.execute(sql)
    cur_result = cursor.fetchall()
    cursor.close()
    db.close()
    return cur_result

def db_exe(sql):
    db = pymysql.connect("mysql_test", "root", "Vudo3423", "HiDockerwifi")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

