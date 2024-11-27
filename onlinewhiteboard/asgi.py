import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

try:
    from draw.urls import websocket_urlpatterns
    print("WebSocket URL patterns imported successfully!")
except ImportError as e:
    print(f"Error importing websocket_urlpatterns: {e}")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinewhiteboard.settings')
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # This handles HTTP requests
    "websocket": URLRouter(websocket_urlpatterns),  # Use the imported WebSocket routes
})


