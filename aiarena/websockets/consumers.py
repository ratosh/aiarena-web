import json

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    # def receive(self, text_data=None, bytes_data=None):
    def receive(self, text_data, **kwargs):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))


class HeartbeatConsumer(WebsocketConsumer):
    """
    Option 1: Rely on the in-built websocket heartbeat.
    Need to find out when disconnect is fired and whether this will server our purpose.
    If disconnect is fired when a websocket times out, when this could be our heartbeat.
    Option 2: use message sending as our heartbeat - a reliable fallback.
    """
    # todo: ensure arena clients can only register a heartbeat for matches they're assigned to.
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        pass
