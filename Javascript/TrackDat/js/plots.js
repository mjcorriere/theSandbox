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

	data = []

	trackDat.laps.forEach( function(lap) {

		data.push({
			key: 'Lap #' + lap.lapID,
			values: lap.gg,
			color: '#CC0000'
		});

	})

	return data;

}

function initCharts() {

	nv.addGraph( function() {
		
		ggPlot = nv.models.scatterChart();

		ggPlot.showLegend(false);

		ggPlot.xDomain([-2, 2]);
		ggPlot.yDomain([-2, 2]);

		ggPlot.xAxis
			.axisLabel('Lateral G')
			.tickFormat( d3.format('.01f'));

		ggPlot.yAxis
			.axisLabel('Longitudinal G')
			.axisLabelDistance(30)
			.tickFormat( d3.format('.01f'));

		ggPlot.margin(
			{left: 75}
		);

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
			.tickFormat(d3.format('d'));

		lineChart.yAxis
			.axisLabel('Velocity (km/h)')
			.axisLabelDistance(40)
			.tickFormat(d3.format('d'));

		// lineChart.yDomain([0, 200]);

		lineChart.y2Axis
			.tickFormat(d3.format('d'));			

		lineChart.margin(
			{left: 50}
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

function updateCharts() {

	d3.select('#ggplot')
		.datum(scatterData)
		.call(ggPlot);

	d3.select('#linechart')
		.datum(plotData)
		.call(lineChart);	

}