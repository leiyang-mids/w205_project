//Defining map as a global variable to access from //other functions
var map;
function initMap() {
//Enabling new cartography and themes
google.maps.visualRefresh = true;

//Setting starting options of map
var cityLat = 39.98;
var cityLng = 116.318;
var mapOptions = {
  center: new google.maps.LatLng(cityLat, cityLng),
  zoom: 10,
  mapTypeId: google.maps.MapTypeId.ROADMAP
};

//Getting map DOM element
var mapElement = document.getElementById('mapDiv');

//Creating a map with DOM element which is just //obtained
map = new google.maps.Map(mapElement, mapOptions);
//create the heatmap layer
var heatmapPoints = [];
//30.2671500, -97.7430600
//39.984702; longitude:116.318417
var cityLat = 39.98;
var cityLng = 116.318;

for ( var i=0;i < 1000;i++) {
  var latLng = new google.maps.LatLng(cityLat+Math.random()/5,cityLng+Math.random()/5);
  var weightedLoc = {
    location:latLng,
    weight:0.5*Math.random()
  };
  heatmapPoints.push(weightedLoc);
}
var heatmap = new google.maps.visualization.HeatmapLayer({
      data: heatmapPoints
});
//add the heatmap layer to the map
heatmap.setMap(map);
}
google.maps.event.addDomListener(window, 'load', initMap);
