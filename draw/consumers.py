import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CanvasConsumer(AsyncWebsocketConsumer):
    # Shared dictionary to store canvas states for each slug
    canvas_states = {}

    async def connect(self):
        # Extract the slug from the URL
        self.slug = self.scope['url_route']['kwargs']['slug']
        self.room_group_name = f"canvas_{self.slug}"

        # Join the slug-specific group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # Send the current canvas state to the newly connected user
        current_state = self.canvas_states.get(self.slug)
        if current_state:
            await self.send(text_data=json.dumps({
                'action': 'update',
                'payload': current_state,
            }))

    async def disconnect(self, close_code):
        # Leave the slug-specific group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json.get('action')
        payload = text_data_json.get('payload')

        if action == 'update':
            # Update the stored canvas state for this slug
            self.canvas_states[self.slug] = payload

        # Broadcast the message to the slug-specific group
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
