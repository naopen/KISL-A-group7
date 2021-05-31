window.onload = function(){
    var now = new Date();

    var addZero = function(value) {
        if (value < 10) {
            value = '0' + value;
            }
        return value;
    };

    var seconds = now.getSeconds();
    var minutes = now.getMinutes();
    var hours = now.getHours();
    seconds = addZero(seconds);
    minutes = addZero(minutes);
    hours = addZero(hours);

    document.getElementById('currentTime').innerHTML = hours + ':' + minutes + ':' + seconds;
};

/*
(timer)ミリ秒毎にページを更新するプログラム

const timer = 10000
window.addEventListener('load',function(){
    setInterval('location.reload()',timer)
});
*/

//更新ボタン
function koushin(){
    location.reload();
}