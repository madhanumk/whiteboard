import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CanvasConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "canvas_updates"

        # Join the group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json.get('action')
        payload = text_data_json.get('payload')

        # Broadcast the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'canvas_update',
                'action': action,
                'payload': payload,
            }
        )

    async def canvas_update(self, event):
        action = event['action']
        payload = event['payload']

        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'action': action,
            'payload': payload,
        }))
