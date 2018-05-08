

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
    rng = pd.date_range('1/1/2011', periods=7500, freq='H')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)

    graphs = [
        dict(
            data=[
                dict(
                    x=[1, 2, 3],
                    y=[10, 20, 30],
                    type='scatter'
                ),
            ],
            layout=dict(
                title='first graph'
            )
        ),

        dict(
            data=[
                dict(
                    x=[1, 3, 5],
                    y=[10, 50, 30],
                    type='scatter'
                ),
            ],
            layout=dict(
                title='second graph'
            )
        ),

        dict(
            data=[
                dict(
                    x=ts.index,  # Can use the pandas data structures directly
                    y=ts
                )
            ]
        )
    ]

    # Add "ids" to each of the graphs to pass up to the client
    # for templating
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html',
                           ids=ids,
                           graphJSON=graphJSON)
    #return render_template("index.html")

# the route to execute the query
@app.route('/_incoming-query')
def find_incoming():
    """get wallet address for query"""
    print(request.args)
    wallet = request.args.get('wallet')
    stmt = "select count(*) as cnt, sum(amt) as sm, to_wallet from txns4 where from_wallet=%s group by to_wallet;"
    response = session.execute(stmt, parameters=[wallet])
    response_list = []
    for val in response:
        response_list.append(val)
    jsonresponse = [{"count": x.cnt,
                     "sum": x.sm,
                     "to_wallet": x.to_wallet} for x in response_list]
    print(jsonresponse)
    return jsonify(result=jsonresponse)







