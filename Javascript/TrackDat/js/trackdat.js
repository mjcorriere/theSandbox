// Track dat
(function(trackDat) {

	var map, drawingManager;
	var reader = new FileReader();

	var intervalID 		= null
		, frame 		= 0
		, trackPath 	= null
		, vehicleSymbol = null
		, delay			= 0
	;

	var laps 			= [];

	var colorArray		= [ '#e74c3c', '#2980b9', '#27ae60', '#e67e22', 
							'#8e44ad', '#34495e', '#c0392b', '#3498db', 
							'#2ecc71', '#16a085', '#f1c40f'
					  		];

	/* Start line state and styling */
	var drawingStartLine 	= false,
		startLineDrawn		= false,
		startLine 			= new google.maps.Polyline({
								strokeColor: 	'#006600',
								strokeOpacity: 	1.0,
								strokeWeight: 	1.5,
								editable: 		true
							});

	/*****
	 * Get handles for all the UI elements / buttons
	 *
	 */

	var drawModeButton 	= document.getElementById('drawModeButton')
		, fileButton 	= document.getElementById('filebutton')
		, fileLoader 	= document.getElementById('fileloader')
		, playButton	= document.getElementById('playButton')
		, stopButton	= document.getElementById('stopButton')
	;

	/****
	 * Tie the event handlers to the appropriate functions
	 *
	 */

	drawModeButton.onclick 	= toggleDrawStartLine;
	playButton.onclick 		= startAnimation;
	stopButton.onclick		= stopAnimation;
	
	fileButton.onclick 		= (function() {
									fileLoader.click();
								});

	fileLoader.onchange		= handleFiles;

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

	function startAnimation() {

		delay = 30;	//ms

		intervalID = window.setInterval(animate, delay);

	}

	function stopAnimation() {

		window.clearInterval(intervalID);

	}

	function animate() {

		console.log('frame no: ' + frame)
		frame = (frame + 1) % 5000;

		var icons = trackPath.get('icons');
		icons[0].offset = (frame / 50) + '%';
		trackPath.set('icons', icons);

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
			'LAPID': 2,
			'LAT': 	9,
			'LNG': 	11,
			'NS': 	10,
			'EW': 	12,
			'SPEED': 14,
		}

		function Lap() {
			
			//Simple object for containing lap info
			//Public Variables

			this.latlng = [];
			this.speed 	= [];
			this.lapID 	= 0;
			this.color  = '#000000';

		}

		var i 				= 0
			colorIndex		= 0
			, currentLap 	= 0
		;
		
		trackDat.laps		= [];

		sessionData.forEach( function(row) {

			// Ensure we are only using good lap data.
			// Lap 0 is before start line is crossed.
			if ( row[indices.LAPID] != 0) {

				lat = row[indices.LAT];
				lng = row[indices.LNG];

				if (row[indices.NS] == 'S') {
					lat = -lat;
				}

				if (row[indices.EW] == 'W') {
					lng = -lng;
				}

				if ( row[indices.LAPID] != currentLap) {

					currentLap = row[indices.LAPID];
					trackDat.laps[currentLap] = new Lap();
					i = 0;

				}

				trackDat.laps[currentLap].latlng.push( new google.maps.LatLng(lat, lng) );
				trackDat.laps[currentLap].speed.push( { x: i, y: +row[indices.SPEED] } );
				trackDat.laps[currentLap].lapID = currentLap;
				trackDat.laps[currentLap].color = colorArray[ colorIndex % colorArray.length ].toUpperCase();

				trackCoordinates.push(
					new google.maps.LatLng(lat, lng)
				);

				trackDat.speed.push({
					x: i,
					y: +row[indices.SPEED] 
				});

				i++;
				colorIndex++;

			}

		});

		vehicleSymbol = {
			path: 			google.maps.SymbolPath.FORWARD_CLOSED_ARROW,
			scale: 			3,
			strokeWeight: 	1.0,
			strokeColor: 	'#000000',
			fillColor: 		'#0022CC',
			fillOpacity: 	1.0
		}

		trackPath = new google.maps.Polyline({

			path: 			trackCoordinates,
			geodesic: 		true,
			strokeColor: 	colorArray[0],
			strokeOpacity: 	.7,
			strokeWeight: 	1.5,
			draggable: 		false,
			icons: [{
				icon: vehicleSymbol,
				offset: '100%'
			}]

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