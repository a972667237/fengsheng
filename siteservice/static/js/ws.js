/**
 * Created by wueiz on 2017/8/1.
 */
function FengshengWebSocket() {
        websocket = new WebSocket("ws://47.52.108.234:1234?uid=602751&subscribe=1&ticks=636371924886132812&stock=&key=e7f518fabdf79fb873cae779ae033f7f");
        websocket.onopen = function(evt) {
            console.log("websocket connect");
        };
        websocket.onclose = function(evt) {
            console.log("websocket close");
        };
        websocket.onmessage = function(evt) {
            if (evt.data[0]=="{") {
                var result = JSON.parse(evt.data);
                var content_array = result.sb;
                content_array.forEach(e => realTimeInformation[e.n] = e.v);
            }
        };
        websocket.onerror = function(evt) {
            console.log("error");
        };
}


var realTimeInformation = {};
FengshengWebSocket();

function updatePrice() {
    $list_content = $(".price tr");
    $list_content[1].children[1].innerHTML = dealPrice(realTimeInformation["AUD"]);
    $list_content[2].children[1].innerHTML = dealPrice(realTimeInformation["EUR"]);
    $list_content[3].children[1].innerHTML = dealPrice(realTimeInformation["GBP"]);
    $list_content[4].children[1].innerHTML = dealPrice(realTimeInformation["Gold"]);
    $list_content[5].children[1].innerHTML = dealPrice(realTimeInformation["LLS"]);
    $list_content[6].children[1].innerHTML = dealPrice(realTimeInformation["Oil"]);
    $list_content[7].children[1].innerHTML = dealPrice(realTimeInformation["USD"]);
    setTimeout(updatePrice, 3000);
}

function dealPrice(p) {
    if(typeof p == "undefined"){
        p = "正在更新";
    } else {
        p = p.toFixed(4);
    }
    return p;
}

setTimeout(updatePrice, 3000);