
// Use anonymous function to submit form to flask 
// for querying data from cassandra.
// Then, receive the data from flask from cassandra
// When the form is submitted, create a continuous query
/*$(function() {
    var submit_form = function(e) {
        $.getJSON($SCRIPT_ROOT + '/_query', {
            a: $('input[name="a"]').val(),
            b: $('input[name="b"]').val()
        }, function(data) {
            makePlotly(data.result);
        });
        return false;
    };
    $('button#calculate').bind('click', submit_form);
    $('input[type=text]').bind('keydown', function(e) {
        if (e.keyCode == 13) {
            submit_form(e);
        }
    });
});*/

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
// This is the function that will continue to run at 10s interval.
/*
function continuousQ() {
    setInterval(call, 10000);
};
*/


// This is the function that will actually do the query.
function call() {
    $.getJSON($SCRIPT_ROOT + '/_query', {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val()
    }, function(data) {
        makePlotly(data.result);
    });
    return false;
};


var colors = ['6600CC',	'FFCC00', '000000', 'CC0000']


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

    console.log(x);
    console.log(y);



    // get the DOM object for plotting
    var plotDiv = document.getElementById("chart1");
    var traces = [{
        x: x,
        y: y,
        mode: 'markers',
        type: 'scatter',
        name: 'Team A',
        text: z,
        size: 4
    }];

    // Draw the window box
    shapes = [];
    for (var i=0; i<bound.length/2; i++) {
        shapes.push({
            type: 'scatter',
            // x-reference is assigned to the x-values
            xref: 'x',
            // y-reference is assigned to the y-values
            yref: 'y',
            x0: x[bound[2*i]],
            y0: mean[bound[2*i]] - 2 * std[bound[2*i]],
            x1: x[bound[2*i+1]],
            y1: mean[bound[2*i]] + 2 * std[bound[2*i]],
            fillcolor: colors[i%4],
            opacity: 0.2,
            line: {
                width: 0
            }
        });
    }

    // Compose layout
    var layout = {
  
        shapes,
        //title: 'User ID '+$('input[name="a"]').val()+' (refresh every 10 s)',
        yaxis: {
            title: 'Bitcoins'
        }

    }

    if (chartType == 'incoming') {
        Plotly.newPlot('chart1', traces);
    }
    else if (chartType == 'outgoing') {
        Plotly.newPlot('chart2', traces);
    }

};
