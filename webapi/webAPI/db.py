import pymysql
import json

def get_data_from_db(host,port,db,sql):
    """
    get data from database
    """
    conn = pymysql.connect(host=host,user='root',passwd='Vudo3423',port=port,db=db)
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def send_to_db(host,port,db,sql):
    """
    save data to database
    """
    conn = pymysql.connect(host=host,user='root',passwd='Vudo3423',port=port,db=db)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def get_user_info(host,port):
    """
    get user information from database
    """
    db = 'userdb'
    sql = 'select * from user_info_db'
    
    data = get_data_from_db(host,port,db,sql)
    dict = {}
    for list in data:
        dict[list[1]] = list[2]
    data_json = json.dumps(dict)
    return data_json

def get_host_port(UUID):
    """
    get the host and port that link from this UUID
    """
    host = 'test-mysql'
    port = 3306
    sql = 'select * from equip_to_db where UUIDS="' + UUID +'"'
    db = 'iot_db'
    data = get_data_from_db(host,port,db,sql)
    userdb = data[0][1]
    uuids = data[0][2]
    notes = data[0][3]
    host = data[0][4]
    port = data[0][5]
    data = {"userdb":userdb,"uuids":uuids,"notes":notes,"host":host,"port":port}
    data_json = json.dumps(data)
    return data_json

def get_user_equip(host,port):
    """
    get the equip that is working
    """
    db = 'userdb'
    sql = 'select * from user_equip_db'
    dict = {}
    data = get_data_from_db(host,port,db,sql)
    for list in data:
        dict[list[1]] = {'UUIDS':list[2],'VAL':list[3],'NOTES':list[4]}
    
    data_json = json.dumps(dict)
    return data_json

def get_user_monitor(host,port):
    """
    get the monitor's data
    """
    db = 'userdb'
    sql = 'select * from user_monitor_db'
    dict = {}
    data = get_data_from_db(host,port,db,sql)
    for list in data:
        dict[list[1]] = {'VAL':list[2],'NOTES':list[3]}

    data_json = json.dumps(dict)
    return data_json

def get_iot_monitor(host,port):
    """
    get the monitor's data of iot
    """
    db = 'iot_db'
    sql = 'select * from iot_monitor_db'
    dict = {}
    data = get_data_from_db(host,port,db,sql)
    for list in data:
        dict[list[1]] = {'VAL':list[2],'NOTES':list[3]}
    
    data_json = json.dumps(dict)
    return data_json

def get_iot_equip(host,port):
    db = 'iot_db'
    sql = 'select * from iot_equip_db'
    dict = {}
    data = get_data_from_db(host,port,db,sql)
    for list in data:
        dict[list[1]] = {'UUIDS':list[2],'VAL':list[3],'NOTES':list[4]}
    data_json = json.dumps(dict)
    return data_json

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 12306
    db = 'userdb'
    sql = 'select * from user_info_db'
    print get_user_info(host,port)
