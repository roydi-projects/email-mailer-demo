from email_provider import EmailProvider
from repo import DBRepo

class Mailer:
    def __init__(self):
        self.next_id = 1
        self.db = DBRepo()
        self.email_provider = EmailProvider(self.db)

    def send(self, message_obj):
        message_obj['id'] = self.next_id
        message_obj['status'] = 'waiting'
        self.next_id += 1
        self.db.insert(message_obj['id'], message_obj)
        self.email_provider.add_to_queue(message_obj)
        return message_obj['id']

    def cancel(self, message_id):
        self.db.set(message_id, 'status', 'deleted')
        