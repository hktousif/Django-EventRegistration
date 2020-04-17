var countDownDate = new Date("Jan 01, 2021 00:00:00").getTime();

    var x = setInterval(function() {

  var now = new Date().getTime();

 var distance = countDownDate - now;
    
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    if (distance < 0) {
        document.getElementById("dd").innerHTML = -days-1;
        document.getElementById("hh").innerHTML =-hours-1;
        document.getElementById("mm").innerHTML = -minutes-1;
        document.getElementById("ss").innerHTML =-seconds-1;
    }
    else{
        document.getElementById("dd").innerHTML = days;
        document.getElementById("hh").innerHTML =hours;
        document.getElementById("mm").innerHTML = minutes;
        document.getElementById("ss").innerHTML =seconds;
    }
  
}, 1000);