import pydb
import time
import os

def getSubgroup():
    sql = "select group_name from group_table"
    cluster_list = []
    sql_result = pydb.db_get(sql, "Group_data")
    for item in sql_result:
        cluster_list.append(item[0])
    return cluster_list

def getDevice(cluster):
    sql = "select subgroup_name from " + cluster
    subcluster_list = []
    sql_result = pydb.db_get(sql, "Group_data")
    for item in sql_result:
        subcluster_list.append(item[0])
    status_sum = 0
    device_sum = 0
    for item in subcluster_list:
        sql = "select e_status from " + item
        sql_result = pydb.db_get(sql, cluster)
        for core in sql_result:
            status_sum += int(core[0])
            device_sum += 1
    return device_sum, status_sum


if __name__ == "__main__":
    #cluster_list = getSubgroup()
   # print(cluster_list)
    print(getDevice("cluster1"))
    #while True:
     #   sql = "select group_name from group_table"
      #  cluster_list = pydb.db_get(sql, "Group_data")
       # print(cluster_list)
        
        
        
        #popu1 = pydb.db_get(sql_popu, "Group_data")[0][0]
        #bir1 = pydb.db_get(sql_birth, "Group_data")[0][0]
        #dea1 = pydb.db_get(sql_death, "Group_data")[0][0]
        
        #time.sleep(600) 
        #pydb.db_exe(sql_update, "Group_data")
