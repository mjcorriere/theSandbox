// Track dat
(function(trackDat) {

	var map, drawingManager;
	var reader = new FileReader();

	/* Start line state and styling */
	var drawingStartLine 	= false,
		startLineDrawn		= false,
		startLine 			= new google.maps.Polyline({
								strokeColor: '#006600',
								strokeOpacity: 1.0,
								strokeWeight: 1.5,
								editable: true
							});

	/*****
	 * Get handles for all the UI elements / buttons
	 *
	 */

	var drawModeButton = document.getElementById('drawModeButton')
		, fileButton = document.getElementById('filebutton')
		, fileLoader = document.getElementById('fileloader');

	/****
	 * Tie the event handlers to the appropriate functions
	 *
	 */

	drawModeButton.onclick = toggleDrawStartLine;
	
	fileButton.onclick = (function() {
		fileLoader.click();
	});

	fileLoader.onchange = handleFiles;

	var sessionData 		= []
		, trackCoordinates 	= [];
	
	// Needs to be public temporariliy for access from plots.js
	trackDat.speed 			= [];	

	/********
	 * Google map initialiation.
	 *
	 *@param: _mapOptions
	 */

	 trackDat.init_map = function(_mapOptions) {
	 	
	 	// Set the map style and initial values
	 	var mapOptions = _mapOptions || {
		 		zoom: 		14
		 		, center: 	new google.maps.LatLng(40.8054567,-73.9654747)
		 		, mapTypeId: 	google.maps.MapTypeId.ROADMAP
		 		, disableDefaultUI: true
	 	};

		// Initialize private map variable
		map = new google.maps.Map( document.getElementById("gmap_canvas"), mapOptions );

		// Setup the drawingManager object

		drawingManager = new google.maps.drawing.DrawingManager({
			
			drawingMode: google.maps.drawing.OverlayType.POLYLINE,
			drawingControl: false,

			polyLineOptions: {
				strokeColor: '#00CC00',
				strokeWeight: 2.5,
				editable: true,
				clickable: false
			}
		});

	}

	function handleFiles() {

		var file = fileLoader.files[0];

		reader.onload = uploadComplete;
		reader.readAsText(file);

	}

	function handleClick(event) {

		console.log('handling click');

		if ( (startLineDrawn == false) && drawingStartLine ) {
			addStartLatLng(event);
		}

	}

	function toggleDrawStartLine() {
		console.log('toggling draw start line');
		drawingStartLine = !drawingStartLine;

		if (drawingStartLine) {
			setLineDrawOn();
		} else {
			setLineDrawOff();
		}

	}

	function setLineDrawOn() {
		//drawingManager.setMap(map);
		drawModeButton.style.backgroundColor = '#CC0000';
	}

	function setLineDrawOff() {
		//drawingManager.setMap(null);
		console.log('draw off');
		drawModeButton.style.backgroundColor = null;
	}	
		
	function addStartLatLng(event) {

		var path = startLine.getPath();

		if (path.length >= 2) {
			return;
		} else {
			path.push(event.latLng);
			if (path.length >= 2) {
				startLineDrawn = true;
				drawingStartLine = !drawingStartLine;
				setLineDrawOff();
			}
		}

	}

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

	function uploadComplete() {

		// File has been uploaded. Let's parse it immediately.
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
			'EW': 	12,
			'SPEED': 14,
		}

		var i = 0;

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

				trackDat.speed.push({
					x: i,
					y: +row[indices.SPEED] 
				});

				i++;

			}

		});

		trackPath = new google.maps.Polyline({

			path: 			trackCoordinates,
			geodesic: 		true,
			strokeColor: 	'#CC0000',
			strokeOpacity: 	.7,
			strokeWeight: 	1.5,
			draggable: 		false

		});

		var bounds = new google.maps.LatLngBounds();

		trackCoordinates.forEach( function(latLng) {
			bounds.extend( latLng );
		});


		map.fitBounds( bounds );
		trackPath.setMap( map );

		// Listen for click events so we can do cool stuff.
		google.maps.event.addListener(map, 'click', handleClick);

		startLine.setMap(map);

		addCharts();

	}	

})(window.trackDat = window.trackDat || {})

/******
 * Initialize the google map on window load
 *
 */
google.maps.event.addDomListener(window, 'load', function() { trackDat.init_map(); } );