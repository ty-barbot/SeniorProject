jQuery(document).ready(function () {
    const container = document.getElementById('container');
    const text = document.getElementById('text');

    const totalTime = 7500;
    const breatheTime = (totalTime / 5) * 2;
    const holdTime = totalTime / 5;
    var minutesLabel = document.getElementById("minutes");
    var secondsLabel = document.getElementById("seconds");
    var totalSeconds = 0;

    breathAnimation();

    function startTimer() {
       var myVar = setInterval(setTime, 1000);
    }

    function setTime() {
        ++totalSeconds;
        secondsLabel.innerHTML = pad(totalSeconds % 60);
        minutesLabel.innerHTML = pad(parseInt(totalSeconds / 60));
    }
    function stopTimer(){
        clearInterval(myVar);
    }

    function pad(val) {
        var valString = val + "";
        if (valString.length < 2) {
            return "0" + valString;
        } else {
            return valString;
        }
    }

    function breathAnimation() {
        jQuery("#text").text('Inhale');
        container.className = 'container grow';

        setTimeout(() => {
            jQuery("#text").text('Hold');

            setTimeout(() => {
                jQuery("#text").text('Exhale');
                container.className = 'container shrink';
            }, holdTime);
        }, breatheTime);
    }

setInterval(breathAnimation, totalTime);
/*function setTimer(){
  ++totalSeconds;
  seconds.innerHTML = pad(totalSeconds %60);
  minutes.innerHTML = pad(parseInt(totalTime / 60));
}

function pad(val){
  var valString = val + "";
  if (valString = val + ""){
    return"0" + valString;
  }
  else{
    return valString;
  }
}*/

});

