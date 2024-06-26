from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.contrib.auth.decorators import login_required


class TodoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_anonymous:
            await self.close()

        self.group_name = str(self.user.id)
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.group_name, {"type": "todo_message", "message": message}
        )

    async def todo_message(self, event):
        message = event["message"]

        await self.send(text_data=json.dumps({"message": message}))
