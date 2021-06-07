var addZero = function(value) {
    if (value < 10) {
        value = '0' + value;
        }
    return value;
};

function showClock() {
    var now = new Date();

    var seconds = now.getSeconds();
    var minutes = now.getMinutes();
    var hours = now.getHours();
    seconds = addZero(seconds);
    minutes = addZero(minutes);
    hours = addZero(hours);

    document.getElementById('currentTime').innerHTML = hours + ':' + minutes + ':' + seconds;
}

window.onload = function(){
    setInterval('showClock()',1000);
};


/*更新ボタン
function koushin(){
    location.reload();
}
*/