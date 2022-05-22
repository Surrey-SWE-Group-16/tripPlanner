var google = undefined;
var googleMapDiv = undefined;
var checkbox_counter = 1; //Initial field counter is 1

window.onload = ()=>{
google = window.google;
initMap()
}
function get_loc_org() {
    $.ajax(
    {
        type:"GET",
        url: "/ajax/get_maps/",
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type':'application/json'
        },
        method: 'GET',
        dataType: 'json',
        data:{
            location: document.getElementById('origin').value
        },
        success: function( data )
        {

            console.log("data is: ", data);
            la = data.results[0].geometry.location.lat;
            lo = data.results[0].geometry.location.lng;
            address = data.results[0].formatted_address;
            weather_api(lo,la, address);
        },
        error: function (request, status, error) {
            console.log("data is: ", error);
        }
     })
}
function get_loc_dest() {
    $.ajax(
    {
        type:"GET",
        url: "/ajax/get_maps/",
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type':'application/json'
        },
        method: 'GET',
        dataType: 'json',
        data:{
            location: document.getElementById('end').value
        },
        success: function( data )
        {

            console.log("data is: ", data);
            la_dest = data.results[0].geometry.location.lat;
            lo_dest = data.results[0].geometry.location.lng;
            address_dest = data.results[0].formatted_address;
            weather_api_dest(lo_dest,la_dest, address_dest);
        },
        error: function (request, status, error) {
            console.log("data is: ", error);
        }
     })
}


function weather_api_dest(lo_dest, la_dest, address_dest){
    $.ajax(
    {
        type:"GET",
        url: "/ajax/weather_api/",
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type':'application/json'
        },
        method: 'GET',
        dataType: 'json',
        data:{
            longitude: lo_dest,
            latitude: la_dest,

        },
        success: function( data )
        {

            document.getElementById("weather_title2").innerHTML = data["name"];
            document.getElementById("weather_sub_title2").innerHTML = data.main.temp +"℃";
            document.getElementById("discrip2").innerHTML = data.weather[0].description;



            console.log("data is: ", data);
        },
        error: function (request, status, error) {
            console.log("data is: ", error);
        }
     })

}
function weather_api(lo, la, address){
    $.ajax(
    {
        type:"GET",
        url: "/ajax/weather_api/",
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type':'application/json'
        },
        method: 'GET',
        dataType: 'json',
        data:{
            longitude: lo,
            latitude: la,

        },
        success: function( data )
        {

            document.getElementById("weather_title").innerHTML = data["name"];
            document.getElementById("weather_sub_title").innerHTML = data.main.temp +"℃";
            document.getElementById("discrip").innerHTML = data.weather[0].description;



            console.log("data is: ", data);
        },
        error: function (request, status, error) {
            console.log("data is: ", error);
        }
     })

}

 function initMap() {


          const directionsService = new google.maps.DirectionsService();
          const directionsRenderer = new google.maps.DirectionsRenderer();
          // Google Maps element in whichlayers will be drawn with Google Maps Javascript API
          googleMapDiv = new google.maps.Map(document.getElementById('googledivMap') ,
          {
            //Deck.gl map Configs and style
            center: { lat: 38.7505686, lng: -9.3963843 },
            minZoom: 3,
            zoom: 13,
            clickableIcons: false,
            disableDefaultUI: true,
            zoomControl: true,
            styles: [
                {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
                {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
                {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
                {
                  featureType: 'administrative.locality',
                  elementType: 'labels.text.fill',
                  stylers: [{color: '#d59563'}]
                },
                {
                  featureType: 'poi',
                  elementType: 'labels.text.fill',
                  stylers: [{color: '#d59563'}]
                },
                {
                  featureType: 'poi.park',
                  elementType: 'geometry',
                  stylers: [{color: '#263c3f'}]
                },
                {
                  featureType: 'poi.park',
                  elementType: 'labels.text.fill',
                  stylers: [{color: '#6b9a76'}]
                },
                {
                  featureType: 'road',
                  elementType: 'geometry',
                  stylers: [{color: '#38414e'}]
                },
                {
                  featureType: 'road',
                  elementType: 'geometry.stroke',
                  stylers: [{color: '#212a37'}]
                },
                {
                  featureType: 'road',
                  elementType: 'labels.text.fill',
                  stylers: [{color: '#9ca5b3'}]
                },
                {
                  featureType: 'road.highway',
                  elementType: 'geometry',
                  stylers: [{color: '#746855'}]
                },
                {
                  featureType: 'road.highway',
                  elementType: 'geometry.stroke',
                  stylers: [{color: '#1f2835'}]
                },
                {
                  featureType: 'road.highway',
                  elementType: 'labels.text.fill',
                  stylers: [{color: '#f3d19c'}]
                },
                {
                  featureType: 'transit',
                  elementType: 'geometry',
                  stylers: [{color: '#2f3948'}]
                },
                {
                  featureType: 'transit.station',
                  elementType: 'labels.text.fill',
                  stylers: [{color: '#d59563'}]
                },
                {
                  featureType: 'water',
                  elementType: 'geometry',
                  stylers: [{color: '#17263c'}]
                },
                {
                  featureType: 'water',
                  elementType: 'labels.text.fill',
                  stylers: [{color: '#515c6d'}]
                },
                {
                  featureType: 'water',
                  elementType: 'labels.text.stroke',
                  stylers: [{color: '#17263c'}]
                }
              ]
          });

          directionsRenderer.setMap(googleMapDiv);
          const onChangeHandler = function () {
            calculateAndDisplayRoute(directionsService, directionsRenderer);
          };

          (document.getElementById("origin")).addEventListener(
              "change",
              onChangeHandler
          );

          (document.getElementById("end")).addEventListener(
            "change",
            onChangeHandler
          );

 }
 function calculateAndDisplayRoute(directionsService,directionsRenderer){

  const waypts = [];
  const elementList = document.querySelectorAll(".stop");
  console.log("elem is ", elementList);
  elementList.forEach(e => {
        waypts.push({
            location: e.value,
            stopover: false,
        });
  });



  directionsService
    .route({
      origin: {
        query: (document.getElementById('origin').value),
      },
      destination: {
        query: (document.getElementById('end').value),
      },
      waypoints: waypts,
      travelMode: google.maps.TravelMode.DRIVING,
    })
    .then((response) => {
      directionsRenderer.setDirections(response);
    })
    .catch((e) => window.alert("Directions request failed due to " + status));
}
function add_check(){
      //Check maximum number of input fields
      $(".content-box-wrapper").append('<div id=""><input type="checkbox" name="check" id="'+checkbox_counter+'" value=""><label for="'+checkbox_counter+'" style="color: black;"> '+document.getElementById('check-name').value+'</label><a onclick="remove_check(this)" class="remove_button"><img src="remove-icon.png"/></a></div><br>'); //Add field html
      checkbox_counter++; //Increment field counter
};

            //Once remove button is clicked
function remove_check(e){
        e.parentElement.remove(); //Remove field html
        checkbox_counter--; //Decrement field counter
};