
//Defining map as a global variable to access from //other functions
/*globals google firstLatLng:true*/
/*eslint-env jquery */
var map;
var heatmap;
var heatmapPoints = [];
var segmentHeatmapPoints = [];
function getSelectedText(elementId) {
    var elt = document.getElementById(elementId);

    if (elt.selectedIndex == -1)
        return null;

    return elt.options[elt.selectedIndex].text;
}
function initMap() {
        //Enabling new cartography and themes
        google.maps.visualRefresh = true;


        //Setting starting options of map at colorado
        //var myLat=38.883956
        //var myLng=-107.552172
         var myLat=37.279518
         var myLng=-121.8863

        var mapOptions = {
          center: new google.maps.LatLng(myLat, myLng),
          zoom: 8,
          mapTypeId: google.maps.MapTypeId.ROADMAP,
          panControl: true,
          scaleControl: false,
          zoomControl: true,
          zoomControlOptions: {
            style: google.maps.ZoomControlStyle.SMALL
          },
          overviewMapControl: true,
          overviewMapControlOptions: {
            opened: true
          },
          mapTypeControl: true,
          mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, google.maps.MapTypeId.HYBRID],
            style: google.maps.MapTypeControlStyle.DROPDOWN_MENU
          }
        };

        //Getting map DOM element
        var mapElement = document.getElementById('mapDiv');

        //Creating a map with DOM element which is just //obtained
        map = new google.maps.Map(mapElement, mapOptions);
        //create the heatmap layer

        heatmap = new google.maps.visualization.HeatmapLayer({
              data: heatmapPoints
        });
        //add the heatmap layer to the map
        heatmap.setMap(map);

        var bicyclingLayer = new google.maps.BicyclingLayer ();
        bicyclingLayer.setMap(map);

        map.enableKeyDragZoom({
    	    visualEnabled: true,
    	    visualPosition: google.maps.ControlPosition.LEFT,
    	    visualPositionOffset: new google.maps.Size(35, 0),
    	    visualPositionIndex: null,
    	    visualSprite: 'http://maps.gstatic.com/mapfiles/ftr/controls/dragzoom_btn.png',
    	    visualSize: new google.maps.Size(20, 20),
    	    visualTips: {
    	        off: "Turn on",
    	        on: "Turn off"
    	    }
    	  });
        var geocoder = new google.maps.Geocoder();
        document.getElementById('submit').addEventListener('click', function() {
          geocodeAddress(geocoder, map);
        });

        $.getJSON("json_file/segments.json",function(segments) {
            //  alert(segments)
           for ( var key in segments ) {
               value=segments[key]
               //alert(value)
               $('#selectid').append(
                   $('<option>').text(value).attr('value',value)
                );
           }
        });

        document.getElementById('submit2').addEventListener('click', function() {
                  selected= getSelectedText('selectid');
                  //alert(selected)
		  segmentAddress(selected);
        });

}


function geocodeAddress(geocoder, resultsMap) {
	var address = document.getElementById('address').value;
	geocoder.geocode({'address': address}, function(results, status) {
		if (status === google.maps.GeocoderStatus.OK) {
			resultsMap.setCenter(results[0].geometry.location);
			var marker = new google.maps.Marker({
				map: resultsMap,
				position: results[0].geometry.location
			});
		}else{
			alert('Geocode was not successful for the following reason: ' + status);
		}
	});
}
//
//
//
function segmentAddress(segment) {
	//create the heatmap layer
	// Read the Json file for locations
	var segmentHeatmapPoints = [];
	var fileName='json_file/locations_'+segment+'.json'
	alert("load the file:"+fileName)
	$.getJSON(fileName, function (data) {
		var locations =data;
		var location, latLng;
		firstLatLng=locations[0];
		for (var i=0;i<locations.length; i++) {
			location = locations[i];
			latLng =new google.maps.LatLng(location.latitude,location.longitude);
			var weightedLoc = {
              location:latLng,
              weight:0.5*Math.random()
            };
            segmentHeatmapPoints.push(weightedLoc);
        }
    })
    //if ( heatmap.getMap() ) {
	 //   heatmap.setMap(null);
    //}
    //alert("Number of coordinates in this segment" + heatmapPoints.length)
    alert("Number of coordinates in this segment" +segmentHeatmapPoints.length)
    //heatmapPoints.push.apply(heatmapPoints,segmentHeatmapPoints)
    heatmapPoints.splice.apply(heatmapPoints,[0,segmentHeatmapPoints].concat(segmentHeatmapPoints));
    heatmapPoints.splice.apply(heatmapPoints,[0,heatmapPoints.length].concat(segmentHeatmapPoints));
    //alert(heatmapPoints.length)
    heatmap.setMap(map)
    //add the heatmap layer to the map
}
//
// helping functions for heat map generations
//
function toggleHeatmap() {
  heatmap.setMap(heatmap.getMap() ? null : map);
}

function changeGradient() {
  var gradient = [
    'rgba(0, 255, 255, 0)',
    'rgba(0, 255, 255, 1)',
    'rgba(0, 191, 255, 1)',
    'rgba(0, 127, 255, 1)',
    'rgba(0, 63, 255, 1)',
    'rgba(0, 0, 255, 1)',
    'rgba(0, 0, 223, 1)',
    'rgba(0, 0, 191, 1)',
    'rgba(0, 0, 159, 1)',
    'rgba(0, 0, 127, 1)',
    'rgba(63, 0, 91, 1)',
    'rgba(127, 0, 63, 1)',
    'rgba(191, 0, 31, 1)',
    'rgba(255, 0, 0, 1)'
  ]
  heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
}

function changeRadius() {
  heatmap.set('radius', heatmap.get('radius') ? null : 20);
}

function changeOpacity() {
  heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
}
