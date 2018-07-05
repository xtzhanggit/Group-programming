import prowo 
import pydb
import sys

def actor_api(command, cluster_id):
    opencps = prowo.Prowo('127.0.0.1', 'Vudo3423', 'host')
    Actor = prowo.Device(opencps, cluster_id)
    result = Actor.do(command)
    return result

def sensor_api(cluster_id):
    opencps = prowo.Prowo('127.0.0.1', 'Vudo3423', 'host')
    Sensor = prowo.Device(opencps, cluster_id)
    result = Sensor.value()
    return result

def class_api(cluster_id):
    sql = "select group_class from group_table where group_name = '" + cluster_id + "'"
    cluster_class = pydb.db_get(sql, 'Group_data')[0][0]
    return cluster_class

if __name__ == '__main__':
    print(sensor_api('cluster3'))
    print(sensor_api('cluster1'))
    print(actor_api(sys.argv[1], 'cluster2'))
    print(class_api('cluster3'), class_api('cluster1'), class_api('cluster2'))

    
