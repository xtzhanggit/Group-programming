import pymysql
import sys
import datetime
def save(sql):
    conn = pymysql.connect('182.254.134.84',user='root',passwd='Vudo3423ljo',port=32306,db='iotdb')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    temp = sys.argv[1]
    humi = sys.argv[2]
    now = datetime.datetime.now()
    strtime = now.strftime('%Y-%m-%d %H:%M:%S') 
    sql = 'insert into dht11 (temperature,humidity,note) values \
            ("' + temp + '","' + humi + '","' + strtime +'")'
    save(sql)

