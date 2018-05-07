

from flask import jsonify, request, redirect, render_template
from flask_socketio import SocketIO, emit

import sys
sys.path.append('/home/ubuntu/flask/app')

from app import app

from cassandra.cluster import Cluster

# setting up connections to cassandra
# setting up connections to cassandra
cluster = Cluster(['35.163.17.140','34.210.159.192','52.13.218.79','54.244.134.26'])
session = cluster.connect("bt2")


# setting up to listen to rethinkDB,
# Then, use socketio to emit to the client side javascript 
   
# the route for the main page
@app.route('/')
def hello():
    return render_template("index.html")

# the route to execute the query
@app.route('/_query')
def add_numbers():
    """get the user id and number of points for query"""
    a = request.args.get('wallet', 0, type=int)
    #stmt = "SELECT userid, time, acc, mean, std, status FROM data WHERE userid=%s limit %s"
    stmt = "select count(*) as cnt, sum(amt) as sm, to_wallet from txns4 where from_wallet = '1LuckyR1fFHEsXYyx5QK4UFzv3PEAepPMK' group by to_wallet;"
    response = session.execute(stmt)
    response_list = []
    for val in response:
        response_list.append(val)
    jsonresponse = [{"count": x.cnt,
                        "sum": x.sm,
                       "to_wallet": x.to_wallet} for x in response_list]
    print(jsonresponse)
    return jsonify(result=jsonresponse)







