

var map;
function initialize() {
  var mapOptions = {
    zoom: 8,
    center: new google.maps.LatLng(-34.397, 150.644),
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
   map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
}



function place_marker(event) {
	pos_x = event.offsetX?(event.offsetX):event.pageX-document.getElementById("pointer_div").offsetLeft;
    pos_y = event.offsetY?(event.offsetY):event.pageY-document.getElementById("pointer_div").offsetTop;
  var marker = new google.maps.Marker({
    position: map.LatLng(pos_y, pos_x)),
    map: map,
    title: 'Click to zoom'
  });

}