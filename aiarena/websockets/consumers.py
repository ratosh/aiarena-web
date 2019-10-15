import json

from channels.generic.websocket import WebsocketConsumer
from ..core.models import Result, Match
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    match_id = 0
    # todo: ensure arena clients can only register a heartbeat for matches they're assigned to.
    def connect(self):
        self.accept()
        match_id = self.scope['url_route']['kwargs']['match_id']

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        if text_data is not None and text_data == 'ping':
            self.send(text_data='pong')
        
@receiver(post_save, sender=Result)
def result_signal_handler(sender, instance, **kwargs):
    if instance.type == 'MatchCancelled':
        pass ##Cancel the match on the client

