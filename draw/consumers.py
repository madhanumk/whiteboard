# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CanvasConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Perform the necessary actions when a WebSocket connection is established
        self.room_name = 'canvas'
        self.room_group_name = f'canvas_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Perform necessary actions when the WebSocket disconnects
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle receiving WebSocket messages
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'canvas_message',
                'message': message
            }
        )

    async def canvas_message(self, event):
        # Send message to WebSocket
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
