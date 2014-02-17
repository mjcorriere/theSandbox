
var drawingStartLine 	= false,
	startLineDrawn		= false,
	startLine = new google.maps.Polyline({
		strokeColor: '#006600',
		strokeOpacity: 1.0,
		strokeWeight: 1.5,
		editable: true
	});

var sessionData = [];
var trackCoordinates = [];

var drawingManager;

var reader = new FileReader();

function handleClick(event) {

	console.log('handling click');

	if ( startLineDrawn == false ) {
		addStartLatLng(event);
	}

}

function toggleDrawStartLine() {
	console.log('toggling draw start line');
	drawingStartLine = !drawingStartLine;
}

function setLineDrawOn() {
	drawingManager.setDrawingMode(google.maps.drawing.OverlayType.POLYLINE);
}

function addStartLatLng(event) {

	var path = startLine.getPath();

	if (path.length >= 2) {
		startLineDrawn = true;
		return;
	} else if (drawingStartLine) {
		path.push(event.latLng);
	}

}

function uploadComplete() {

	sessionData = CSVToArray(reader.result, '\t');

	// Pop the header row
	sessionData.shift();

	// Tab delimited header, for reference
	// ["INDEX", "TRACK ID", "LAP ID", "VALID", "UTC DATE", "UTC TIME", "LOCAL DATE", 
	//		"LOCAL TIME", "MS", "LATITUDE", "N/S", "LONGITUDE", "E/W", "ALTITUDE", 
	//		"SPEED", "HEADING", "G-X", "G-Y", "G-Z"]

	// Elements 10, 11, 12, and 13 are what we are interested in.
	// Lets set up the code to be more readable for Future Mark.

	var indices = {
		'LAT': 	9,
		'LNG': 	11,
		'NS': 	10,
		'EW': 	12
	}

	sessionData.forEach( function(row) {

		// Unsure what this is for. Copied from Nick.
		if ( row[2] != 0) {
			
			lat = row[indices.LAT];
			lng = row[indices.LNG];

			if (row[indices.NS] == 'S') {
				lat = -lat;
			}

			if (row[indices.EW] == 'W') {
				lng = -lng;
			}

			trackCoordinates.push(
				new google.maps.LatLng(lat, lng)
			);

		}

	});

	trackPath = new google.maps.Polyline({

		path: 			trackCoordinates,
		geodesic: 		true,
		strokeColor: 	'#CC0000',
		strokeOpacity: 	1.0,
		strokeWeight: 	1.5,
		draggable: 		false

	});

	map.panTo( trackCoordinates[0] );
	trackPath.setMap(map);

	drawingManager = new google.maps.drawing.DrawingManager({

		drawingMode: null,
		drawingControl: true,
		
		drawingControlOptions: {
			position: google.maps.ControlPosition.TOP_CENTER,
			drawingModes: [

				google.maps.drawing.OverlayType.POLYLINE,

			]
		},

		circleOptions: {
			fillColor: '#ffff00',
			fillOpacity: 1,
			strokeWeight: 5,
			clickable: false,
			zIndex: 1,
			editable: true
		},

		polylineOptions: {
			strokeColor: '00FF00',
			strokeWeight: 2.0,
			editable: true,
			clickable: true
		}

	});

	drawingManager.setMap(map);

	// Listen for click events so we can do cool stuff.
	google.maps.event.addListener(map, 'click', handleClick);
	startLine.setMap(map);

}

function handleFiles() {

	var file = fileLoader.files[0];

	reader.onload = uploadComplete;
	reader.readAsText(file);

}

fileButton = document.getElementById('filebutton');
fileLoader = document.getElementById('fileloader');

drawModeButton = document.getElementById('drawModeButton');


drawModeButton.onclick = toggleDrawStartLine;

fileButton.onclick = (function() {
	fileLoader.click();
});

fileLoader.onchange = handleFiles;

/*
	Nicks copy/pasta magic from the interwebs.
*/

function CSVToArray( strData, strDelimiter ) {

	strDelimiter = (strDelimiter || ",");    

	var objPattern = new RegExp(
		(
			// Delimiters.
			"(\\" + strDelimiter + "|\\r?\\n|\\r|^)" +    
			// Quoted fields.
			"(?:\"([^\"]*(?:\"\"[^\"]*)*)\"|" +    
			// Standard fields.
			"([^\"\\" + strDelimiter + "\\r\\n]*))"
		),
		"gi"
	);        

	var arrData = [[]];    
	var arrMatches = null;        

	// Keep looping over the regular expression matches until we can 
	// no longer find a match.
	while ( arrMatches = objPattern.exec( strData ) )	{    

		// Get the delimiter that was found.
		var strMatchedDelimiter = arrMatches[ 1 ];    

		// Check to see if the given delimiter has a length
		// (is not the start of string) and if it matches
		// field delimiter. If id does not, then we know
		// that this delimiter is a row delimiter.

		if ( strMatchedDelimiter.length && (strMatchedDelimiter != strDelimiter)) {    
	
			// Since we have reached a new row of data, add an empty row to our data array.
			arrData.push( [] );    

		}        
		       
		// Now that we have our delimiter out of the way,
		// let's check to see which kind of value we
		// captured (quoted or unquoted).

		if ( arrMatches[ 2 ] ) {    

			// We found a quoted value. When we capture
			// this value, unescape any double quotes.

			var strMatchedValue = arrMatches[ 2 ].replace(
				new RegExp( "\"\"", "g" ), "\""
			);    
		
		} else {    
			// We found a non-quoted value.
			var strMatchedValue = arrMatches[ 3 ];    
		}        
		     
		// Now that we have our value string, let's add
		// it to the data array.
		arrData[ arrData.length - 1 ].push( strMatchedValue );
		     
	}    

	return( arrData );

};