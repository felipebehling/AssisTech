function disableBtn(){
    let button = document.getElementById("submit_button")
    button.disabled = true
    button.style.opacity = "100"
    button.style.cursor = "pointer"
  }
    
    function iniciarMap(lat, lng){
      let mapa = document.getElementById('map')
      let box = document.getElementsByClassName('register-page')[0]
      // box = box.classList.add('mt-5')
      mapa.style.display = 'block'
      var options = {
        zoom: 15,
        center: {lat: lat, lng: lng}
      }
    var map = new
    google.maps.Map(document.getElementById('map'), options);
  
    var marker = new google.maps.Marker({
      position:{lat: lat, lng: lng},
      map: map,
      icon : ''
    });
  }
  
    
    function getLocation() {
      if ('geolocation' in navigator) {
        navigator.geolocation.getCurrentPosition(
          function(position){
            
            async function getAddress(url = '') {
                        const response = await fetch(url, {
                            method: 'GET',
                        });
                        return response.json(); // parses JSON response into native JavaScript objects
                    }
            
                    getAddress(`https://api.opencagedata.com/geocode/v1/json?q=${position.coords.latitude}+${position.coords.longitude}&key=6714c5e3a132494d8b050ef5498e8356`)
                    .then(data => {
                        console.log(data); // JSON data parsed by `data.json()` call
                        const obj = JSON.stringify(data)
                        const road = data["results"][0]["components"]["road"]
                        const number = data["results"][0]["components"]["house_number"]
                        const city = data["results"][0]["components"]["city"]
                        const district = data["results"][0]["components"]["suburb"]
            
                        document.querySelector('#local').value = `Próximo a ${road} nº ${number} ${district} ${city}`
  
                        iniciarMap(position.coords.latitude, position.coords.longitude)
                        
                    });
            
          }, 
          function(error){
            console.log(error);
          })
        } else {
          alert(".error.")
        }
      }
      