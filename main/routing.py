from channels.routing import route
from . import consumers
from otree.channels.routing import channel_routing

channel_routing += {
    route('websocket.connect', consumers.ws_connect, path=r"^/chat"),
    route('websocket.receive', consumers.ws_receive, path=r"^/chat"),
    route('websocket.disconnect', consumers.ws_disconnect, path=r"^/chat"),
}
