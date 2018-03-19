from channels.routing import route, route_class
from .consumers import ClickConsumer, click_message

click_routing = [
    route_class(ClickConsumer, path=r"^/clicks/(?P<channel>[a-zA-Z0-9_-]+)/$"),
    route('clicktracking.click', click_message),
]
