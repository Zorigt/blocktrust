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
    var x = [], y = [], z = [];


    // retrieve the x as counts, y as sum, z as wallet id
    for (var i=0; i<allRows.length; i++) {
        row = allRows[i];
        x.push( row['count'] );
        y.push( row['sum']/100000000  );
        if (chartType == 'incoming') {
            z.push(row['from_wallet']);
        }
        else if (chartType == 'outgoing') {
            z.push(row['to_wallet']);
        }
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
      title: 'Activities for '+ chartType +' bitcoins',
      xaxis: {
        title: 'Aggregate transactions per wallet'
      },
      yaxis: {
        title: 'Total bitcoins transferred'
      }
    };

    if (chartType == 'incoming') {
        Plotly.newPlot('chart1', traces, layout);
    }
    else if (chartType == 'outgoing') {
        Plotly.newPlot('chart2', traces, layout);
    }

};
