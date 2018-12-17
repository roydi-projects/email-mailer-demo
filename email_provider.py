from threading import Thread
from datetime import datetime
import time
import queue

class EmailProvider:
    def __init__(self, db):
        self.queue = queue.Queue()
        self.start_fetch()
        self.db = db

    def start_fetch(self):
        thread = Thread(target=self.get_next_message)
        thread.daemon = True
        thread.start()

    def add_to_queue(self, message_obj):
        self.queue.put(message_obj)

    def get_next_message(self):
        while True:
            try:
                next_message = self.queue.get(None, False)
                if next_message and self.db.get(next_message['id']).get('status') != 'deleted':
                    print('{datetime} to {to}: {subject}'.format(datetime=datetime.now(), to=next_message['to'], subject=next_message['subject']))
            except queue.Empty:
                pass
            finally:
                time.sleep(1)