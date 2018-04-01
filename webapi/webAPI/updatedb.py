import db
import pymysql 

def send_to_db(host,port,db,sql):
    """
    save data to database
    """
    conn = pymysql.connect(host=host,user='root',passwd='letmein',port=port,db=db)
    cur = conn.cursor()
    conn.select_db(db)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def update_user_info(host,user_name,user_age,user_weight, user_height,user_blood_sugar,user_blood_pressure):
    """
    set user data in database
    """
    sql = 'insert into user_info_db(ID,VAL) values \
          (1,"' + user_name + '"), \
          (2,"' + user_age + '"), \
          (3,"' + user_weight + '"), \
          (4,"' + user_height + '"), \
          (5,"' + user_blood_sugar + '"), \
          (6,"' + user_blood_pressure + '") \
          on duplicate key update VAL=values(VAL)'
    port = 3306
    db = 'userdb'
    send_to_db(host,port,db,sql)

def update_user_monitor(host,port,params,val,notes):
    db = 'userdb'
    sql = 'update user_monitor_db set VAL="' + val + '",NOTES="' + notes + '" where PARAMS="' + params + '"'
    send_to_db(host,port,db,sql)

def update_iot_monitor(host,port,params,val,notes):
    db = 'iot_db'
    sql = 'update iot_monitor_db set VAL="' + val + '",NOTES="' + notes + '" where PARAMS="' + params + '"'
    send_to_db(host,port,db,sql)

def update_iot_equip(host,port,params,uuids,val,notes):
    dbs = 'iot_db'
    sql = 'select * from iot_equip_db where UUIDS="' + uuids + '"'
    data = db.get_data_from_db(host,port,dbs,sql)
    if data == ():
        sql = 'insert into iot_equip_db (PARAMS,UUIDS,VAL,NOTES) values \
               ("' + params + '","' + uuids + '",' + str(val) + ',"' + notes + '")'
        send_to_db(host,port,dbs,sql)
        return 'Success'
    else:
        sql = 'update iot_equip_db set VAL=' + str(val) + ',NOTES="' + notes +'" where UUIDS="' + uuids + '"'
        send_to_db(host,port,dbs,sql)
        return 'Success'

if __name__ == '__main__':
    user_db = 'user_db'
    user_name = 'joliu'
    user_age = '34'
    user_weight = '56'
    user_height = '23' 
    user_blood_sugar = '20'
    user_blood_pressure = '60/120'
    update_user_info(user_db,user_name,user_age,user_weight, user_height,user_blood_sugar,user_blood_pressure)
