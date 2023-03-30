function openNav() {
           document.getElementById("mySidepanel").style.width = "250px";
         }

function closeNav() {
           document.getElementById("mySidepanel").style.width = "0";
         }

function initMap() {
           var map = new google.maps.Map(document.getElementById('map'), {
             zoom: 11,
             center: {lat: 40.645037, lng: -73.880224},
             });
         var image = './static/images/maps-and-flags.png';
         var beachMarker = new google.maps.Marker({
             position: {lat: 40.645037, lng: -73.880224},
             map: map,
             icon: image
           });
         }