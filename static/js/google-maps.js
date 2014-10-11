function update_latlng_controls(latLng) {
     document.getElementById("latitude").value = latLng.lat();
	 document.getElementById("longitude").value = latLng.lng();
}

function initialize() {
    var markers = [];
    var map = new google.maps.Map(document.getElementById('map-canvas'), {
	mapTypeId: google.maps.MapTypeId.ROADMAP,
	disableDoubleClickZoom: true
    });

    google.maps.event.addListener(map, 'dblclick', function (evt) {

	for (var i = 0; i < markers.length; i++) {
	    markers[i].setMap(null);
	}
	markers = [];

        var newMarker = new google.maps.Marker({ position: evt.latLng,
						 map: map,
						 title: 'My Marker',
						 draggable: true
					       });
        markers.push(newMarker);
	update_latlng_controls(evt.latLng);
	google.maps.event.addListener(newMarker, "drag", function (mEvent) {
	    update_latlng_controls(mEvent.latLng);
	    });
    });
    var defaultBounds = new google.maps.LatLngBounds(
	new google.maps.LatLng(-33.8902, 151.1759),
	new google.maps.LatLng(-33.8474, 151.2631));
    map.fitBounds(defaultBounds);

    var input =  document.getElementById('pac-input');
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

    var searchBox = new google.maps.places.SearchBox((input));

    google.maps.event.addListener(searchBox, 'places_changed', function() {
	var places = searchBox.getPlaces();

	if (places.length == 0) {
	    return;
	}

	var bounds = new google.maps.LatLngBounds();
	for (var i = 0, place; place = places[i]; i++) {
	    var image = {
		url: place.icon,
		size: new google.maps.Size(71, 71),
		origin: new google.maps.Point(0, 0),
		anchor: new google.maps.Point(17, 34),
		scaledSize: new google.maps.Size(25, 25)
	    };


	    bounds.extend(place.geometry.location);
	}

	map.fitBounds(bounds);
	map.setZoom(15);
    });

    google.maps.event.addListener(map, 'bounds_changed', function() {
	var bounds = map.getBounds();
	searchBox.setBounds(bounds);
    });
}

google.maps.event.addDomListener(window, 'load', initialize);
