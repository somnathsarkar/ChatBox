from channels.routing import route

channel_routing = [route('websocket.receive','ChatApp.consumers.ws_echo'),route('websocket.connect','ChatApp.consumers.ws_add'),route('websocket.disconnect','ChatApp.consumers.ws_remove'),]