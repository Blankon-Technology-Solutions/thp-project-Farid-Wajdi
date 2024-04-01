import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from todo_list.middleware import TokenAuthMiddleware
import todo_list.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_list.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": TokenAuthMiddleware(
        URLRouter(
            todo_list.routing.websocket_urlpatterns
        )
    ),
})
