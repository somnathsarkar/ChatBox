from ChatApp.models import Message,User
from channels import Group
import datetime
import json
from django.utils import timezone

def ws_echo(message):
    j = json.loads(message.content['text'])
    u = User.objects.get(username = j['sender'])
    r = User.objects.get(username=j['recipient'])
    m = Message(creator_id = u, message_body=j['body'], recipient_id = r, create_date=timezone.now())
    m.save()
    Group('ChatApp').send({"text":"Refresh"})
def ws_add(message):
    Group('ChatApp').add(message.reply_channel)
    message.reply_channel.send({"accept":True})
def ws_remove(message):
    Group('ChatApp').discard(message.reply_channel)