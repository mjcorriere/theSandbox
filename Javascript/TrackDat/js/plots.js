/*

	Create the velocity vs position plot and G/G plot.
	This version currently creates fake data for the plots as placeholders.
	Future version will take data from the filereader at trackdat.js

*/


function plotData() {

	data = [];

	trackDat.laps.forEach( function(lap) {
		data.push({
			key: 'Lap #' + lap.lapID,
			values: lap.speed,
			color: lap.color
		});
	})

	return data;

}

function scatterData() {
	var theData = [];

	for (var i=0; i < 100; i++) {

		theData.push({
			x: (Math.random() * 10) - 5,
			y: (Math.random() * 10) - 5,
		});

	}

	return [
		{
			values: theData,
			color: '#666000'
		}
	];

}

function addCharts() {

	nv.addGraph( function() {
		
		var chart = nv.models.scatterChart();

		chart.showLegend(false);

		chart.xAxis
			.tickFormat( d3.format('.2f'));

		chart.yAxis
			.tickFormat( d3.format('2f'));

		d3.select('#ggplot')
			.datum(scatterData)
			.call(chart)

		nv.utils.windowResize( function() {
			chart.update
		});

		return chart;


	});

	nv.addGraph( function() {
		
		var chart = nv.models.lineWithFocusChart();

		chart.showLegend(false);

		chart.xAxis
			.axisLabel('Track Position')				
			.tickFormat(d3.format('.2f'));

		chart.yAxis
			.axisLabel('The Big Y')
			.tickFormat(d3.format('.2f'));

		// chart.yDomain([0, 200]);

		chart.y2Axis
			.tickFormat(d3.format('.2f'));			

		chart.margin(
			{left: 100}
		);

		chart.height2(50);

		d3.select('#linechart')
			.datum(plotData)
			.call(chart);

		nv.utils.windowResize( function() { 
			chart.update() 
		});
			
		return chart;

	});

}