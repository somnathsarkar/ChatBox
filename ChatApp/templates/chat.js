function js_ws_go(){
	var ws = new WebSocket("ws://127.0.0.1:8000/");
	ws.onmessage = function(){
		location.reload();
	}
	ws.onopen = function(){
	    ws.send("Hello world!");
	}
}