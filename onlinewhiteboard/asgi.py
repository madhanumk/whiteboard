import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from draw import consumers  # Ensure this is the correct path to your consumers module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinewhiteboard.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # This handles HTTP requests
    "websocket": URLRouter([  # WebSocket route without authentication middleware
        path('ws/canvas/', consumers.CanvasConsumer.as_asgi()),  # WebSocket route
    ]),
})
