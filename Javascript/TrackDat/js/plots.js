/*

	Create the velocity vs position plot and G/G plot.
	This version currently creates fake data for the plots as placeholders.
	Future version will take data from the filereader at trackdat.js

*/


var lineChart, ggPlot;

function emptyData() {
	return [{
		values: [{}],
		key: 'No Data'
	}]
}

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

function initCharts() {

	nv.addGraph( function() {
		
		ggPlot = nv.models.scatterChart();

		ggPlot.showLegend(false);

		ggPlot.xAxis
			.tickFormat( d3.format('.2f'));

		ggPlot.yAxis
			.tickFormat( d3.format('2f'));

		d3.select('#ggplot')
			.datum(emptyData)
			.call(ggPlot);

		nv.utils.windowResize( function() {
			ggPlot.update
		});

		return ggPlot;

	});

	nv.addGraph( function() {
		
		lineChart = nv.models.lineWithFocusChart();

		lineChart.showLegend(false);

		lineChart.xAxis
			.axisLabel('Track Position')				
			.tickFormat(d3.format('.2f'));

		lineChart.yAxis
			.axisLabel('The Big Y')
			.tickFormat(d3.format('.2f'));

		// lineChart.yDomain([0, 200]);

		lineChart.y2Axis
			.tickFormat(d3.format('.2f'));			

		lineChart.margin(
			{left: 100}
		);

		lineChart.height2(50);

		d3.select('#linechart')
			.datum(emptyData)
			.call(lineChart);		

		nv.utils.windowResize( function() { 
			lineChart.update() 
		});
			
		return lineChart;

	});	


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

function updateCharts() {

	d3.select('#ggplot')
		.datum(scatterData)
		.call(ggPlot);

	d3.select('#linechart')
		.datum(plotData)
		.call(lineChart);	

}