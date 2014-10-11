var mainMap;
var mainMapMarkers = [];
last_refresh = new Date();
process_wait = false;
wait_between_refresh = 1500; // [ms]

function reload_markers() {
    var bounds = mainMap.getBounds();
    var NE = bounds.getNorthEast();
    var SW = bounds.getSouthWest();
    $.ajax({
        url: "/event/events_from_range/" + NE.lat() + "/" + SW.lat() + "/" + NE.lng() + "/" + SW.lng(),
        context: document.body
        }).done(function(data) {
            load_new_markers(data);
        });
}

function initializeMainMap() {
  var mapOptions = {
    zoom: 8,
    center: new google.maps.LatLng(-34.397, 150.644)
  };
  mainMap = new google.maps.Map(document.getElementById('main-map-canvas'),
      mapOptions);


  google.maps.event.addListener(mainMap, 'bounds_changed', function() {
    new_refresh = new Date();
    diff = Math.abs(last_refresh.getTime() - new_refresh.getTime());
    last_refresh = new_refresh;
    if (diff > wait_between_refresh) {
      reload_markers();
    }
    else if (process_wait == false) {
      process_wait = true;
      setTimeout(function(){reload_markers(); process_wait=false;}, wait_between_refresh - diff);
    }
  });

}

function clear_all_markers() {
for (var i = 0; i < mainMapMarkers.length; i++ ) {
    mainMapMarkers[i].setMap(null);
  }
  mainMapMarkers.length = 0;
}

function load_new_markers(str) {
  clear_all_markers();
  new_latlng = str.split(';');
  for (var i = 0; i < new_latlng.length; i++) {
    new_latlng[i] = new_latlng[i].trim();
    if (new_latlng[i].length == 0)
        continue;
    poses = new_latlng[i].split(',');
    mainMapMarkers.push(new google.maps.Marker({
      position:  new google.maps.LatLng(parseFloat(poses[0]),parseFloat(poses[1])),
      map: mainMap,
      title: 'Hello World!'
  }));

  }
}

google.maps.event.addDomListener(window, 'load', initializeMainMap);

