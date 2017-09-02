from channels.routing import route, include
from drt.tables.consumers import tables_connect, tables_disconnect, tables_message


tables_routing = [
    route("websocket.connect", tables_connect),
    route("websocket.receive", tables_message),
    route("websocket.disconnect", tables_disconnect),
]


channel_routing = [
    include(tables_routing, path=r'^/tables/'),
]