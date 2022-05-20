
function get_loc() {
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
            la = data.result[0].geometry.location.lat
            lo = data.result[0].geometry.location.lng
            weather_api(lo,la);
        },
        error: function (request, status, error) {
            console.log("data is: ", error);
        }
     })
}


function weather_api(lo, la){
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
            latitude: la
        },
        success: function( data )
        {
            document.getElementById('#weather_title').innerHTML = "hello"
            document.getElementById('#weather_title').innerHTML = new HTML
            console.log("data is: ", data);
        },
        error: function (request, status, error) {
            console.log("data is: ", error);
        }
     })

}