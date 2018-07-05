from flask import Flask, request, jsonify
import pydb
import time
import os
import json
from flask_cors import *


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


app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/health_degree', methods = ['POST'])
def getDegree():
    cluster_id_list = json.loads(request.form['cluster_id'])
    cluster_id = cluster_id_list[0]
    number_list = getDevice(cluster_id)
    degree = number_list[1] / number_list[0]
    response = str(degree)
    return response, 200

@app.route('/value', methods = ['POST'])
def getValue():
    cluster_id_list = json.loads(request.form['cluster_id'])
    cluster_id = cluster_id_list[0]
    sql = "select group_value from group_table where group_name = '" + cluster_id + "'"
    value = pydb.db_get(sql, "Group_data")[0][0]
    response = value
    return response, 200

if __name__ == "__main__":
    app.run(threaded = True, debug = True, host = '0.0.0.0', port = 4444)
