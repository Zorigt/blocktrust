

from flask import jsonify, request, redirect, render_template
import pandas as pd
import numpy as np
import json
import plotly
from flask_socketio import SocketIO, emit
import plotly.plotly as py
import plotly.graph_objs as go

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



    return render_template('index.html')
    #return render_template("index.html")

# the route to execute the bitcoin query
@app.route('/_query')
def find_incoming():
    """get wallet address for query"""
    wallet = request.args.get('wallet')
    queryType = request.args.get('queryType')
    if queryType == 'incoming':
        stmt = "select count(*) as cnt, sum(amt) as sm, from_wallet from txns where to_wallet=%s group by from_wallet allow filtering;"
    elif queryType == "outgoing":
        stmt = "select count(*) as cnt, sum(amt) as sm, to_wallet from txns where from_wallet=%s group by to_wallet;"
    response = session.execute(stmt, parameters=[wallet])
    response_list = []
    for val in response:
        response_list.append(val)
    print(response_list)
    if queryType == 'incoming':
        jsonresponse = [{"count": x.cnt,
                         "sum": x.sm,
                         "from_wallet": x.from_wallet} for x in response_list]
        print(jsonresponse)
    elif queryType == 'outgoing':
        jsonresponse = [{"count": x.cnt,
                         "sum": x.sm,
                         "to_wallet": x.to_wallet} for x in response_list]
    return jsonify(result=jsonresponse)








