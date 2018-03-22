from channels.routing import route
import main.consumers
import practice.consumers
from otree.channels.routing import channel_routing
from clicktracking.routing import click_routing

channel_routing += {
    route('websocket.connect', main.consumers.ws_connect, path=r"^/chat"),
    route('websocket.receive', main.consumers.ws_receive, path=r"^/chat"),
    route('websocket.disconnect', main.consumers.ws_disconnect, path=r"^/chat"),
    route('websocket.connect', practice.consumers.ws_connect, path=r"^/practice-chat"),
    route('websocket.receive', practice.consumers.ws_receive, path=r"^/practice-chat"),
    route('websocket.disconnect', practice.consumers.ws_disconnect, path=r"^/practice-chat"),
}

channel_routing += click_routing