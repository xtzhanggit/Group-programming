#:coding:utf-8
from flask import Flask,abort,jsonify
from flask import request
import db,updatedb
import json
from flask_cors import *

app = Flask(__name__)
CORS(app,supports_credentials=True)

@app.route('/todo/api/v1.0/hello/')
def hello():
    return 'hello'

@app.route('/todo/api/v1.0/get_user_info/<host>',methods=['GET'])
def get_user_info(host):
    port = 3306
    data_json = db.get_user_info(host,port)
    data = json.loads(data_json)
    return jsonify(data)

@app.route('/todo/api/v1.0/get_host_port/<uuid>',methods=['GET'])
def get_host_port(uuid):
    data_json = db.get_host_port(uuid)
    data = json.loads(data_json)
    return jsonify(data)

@app.route('/todo/api/v1.0/get_user_equip/<host>',methods=['GET'])
def get_user_equip(host):
    port = 3306
    data_json = db.get_user_equip(host,port)
    data = json.loads(data_json)
    return jsonify(data)

@app.route('/todo/api/v1.0/get_user_monitor/<host>',methods=['GET'])
def get_user_monitor(host):
    port = 3306
    data_json = db.get_user_monitor(host,port)
    data = json.loads(data_json)
    return jsonify(data)

@app.route('/todo/api/v1.0/get_iot_monitor/')
def get_iot_monitor():
    host = 'test-mysql'
    port = 3306
    data_json = db.get_iot_monitor(host,port)
    data = json.loads(data_json)
    return jsonify(data)

@app.route('/todo/api/v1.0/get_iot_equip/')
def get_iot_equip():
    host = 'test-mysql'
    port = 3306
    data_json = db.get_iot_equip(host,port)
    data = json.loads(data_json)
    return jsonify(data)

@app.route('/todo/api/v1.0/update_user_monitor/',methods=['POST'])
def update_user_monitor():
    host = request.form['host']
    port = 3306
    params = request.form['params']
    val = request.form['val']
    notes = request.form['notes']
    updatedb.update_user_monitor(host,port,params,val,notes)
    return 'Success'

@app.route('/todo/api/v1.0/update_iot_monitor/',methods=['POST'])
def update_iot_monitor():
    host = 'test-mysql'
    port = 3306
    params = request.form['params']
    val = request.form['val']
    notes = request.form['notes']
    updatedb.update_iot_monitor(host,port,params,val,notes)
    return 'Success'
    
@app.route('/todo/api/v1.0/update_user_info/',methods=['POST'])
def update_user_info():
    host = request.form['host']
    user_name = request.form['user_name']
    user_age = request.form['user_age']
    user_weight = request.form['user_weight']
    user_height = request.form['user_height']
    user_blood_sugar = request.form['user_blood_sugar']
    user_blood_pressure = request.form['user_blood_pressure']
    updatedb.update_user_info(host,user_name,user_age,user_weight,user_height,user_blood_sugar,user_blood_pressure)
    return 'Success'

@app.route('/todo/api/v1.0/update_iot_equip/',methods=['POST'])
def update_iot_equip():
    host = 'test-mysql'
    port = 3306
    params = request.form['params']
    uuids = request.form['uuids']
    val = request.form['val']
    notes = request.form['notes']
    result = updatedb.update_iot_equip(host,port,params,uuids,val,notes)
    return result
    
@app.route('/login',methods=['POST'])
def login():
    print '*********************'
    id = request.form['id']
    pwd = request.form['pwd']
    title = request.form['title']
    result = {'id':id,'pwd':pwd,'title':title}
    return jsonify(result)

if __name__ == "__main__":
    app.run(threaded=True,debug=True,host='0.0.0.0',port=36666)
