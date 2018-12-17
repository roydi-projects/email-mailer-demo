class DBRepo:
    def __init__(self):
        self.db = {}
    
    def insert(self, id, data):
        self.db[id] = data

    def get(self, id):
        return self.db[id]

    def set(self, id, key, value):
        self.db[id][key] = value
