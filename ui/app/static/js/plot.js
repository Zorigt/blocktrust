// Use anonymous function to submit form to flask
// for querying data from cassandra.
// Then, receive the data from flask from cassandra
// When the form is submitted, create a continuous query

$(function() {
    var submit_form = function(e) {
        $.getJSON($SCRIPT_ROOT + '/_query',
            {
                wallet: $('input[name="wallet"]').val(),
                queryType: 'incoming'
            },
            function(data) {
                makePlotly(data.result, 'incoming');
            });
        return false;
    };
    $('button#calculate-incoming').bind('click', submit_form);

});

$(function() {
    var submit_form = function(e) {
        $.getJSON($SCRIPT_ROOT + '/_query',
            {
                wallet: $('input[name="wallet"]').val(),
                queryType: 'outgoing'
            },
            function(data) {
                makePlotly(data.result, 'outgoing');
            });
        return false;
    };
    $('button#calculate-outgoing').bind('click', submit_form);

});

// This is the function that will take the data from cassandra and update the plot.
function makePlotly( allRows, chartType ){
    console.log(allRows);
    var x = [], y = [], z = [], mean = [], std = [];
    var xBox = [], yBox = [];
    var bound = [];

    // use regex to extract time information
    // var time_pattern = new RegExp("[0-9]{2}:[0-9]{2}:[0-9]{2}", "m");

    for (var i=0; i<allRows.length; i++) {
        row = allRows[i];
        x.push( row['count'] );
        y.push( row['sum']/100000000  );
        z.push( row['to_wallet']);
    }
    x = x.reverse();
    y = y.reverse();
    z = z.reverse();

    //console.log(x);
    //console.log(y);



    // get xy coords for plotting
    var traces = [{
        x: x,
        y: y,
        mode: 'markers',
        type: 'scatter',
        name: 'Team A',
        text: z,
        size: 4
    }];


    // Define layout
    var layout = {
      title: 'Transactions for '+ chartType +' bitcoins',
      xaxis: {
        title: 'Number of transactions'
      },
      yaxis: {
        title: 'Bitcoins'
      }
    };

    if (chartType == 'incoming') {
        Plotly.newPlot('chart1', traces, layout);
    }
    else if (chartType == 'outgoing') {
        Plotly.newPlot('chart2', traces, layout);
    }

};
