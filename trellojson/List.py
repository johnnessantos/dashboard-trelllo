class List:
    def __init__(self, list_json):
        self.list_json = list_json

        self.list_id = None
        self.list_name = None
        self.list_closed = None
        self.list_board_id = None
        self.list_subscribed = None
        self.list_position = None

        self.load()

    def load(self):
        self.list_id = self.list_json['id']
        self.list_name = self.list_json['name']
        self.list_closed = self.list_json['closed']
        self.list_board_id = self.list_json['idBoard']
        self.list_subscribed = self.list_json['subscribed']
        self.list_position = self.list_json['pos']

    def original_json(self):
        return self.list_json

    def json(self):
        return {
            'list_id': self.list_id,
            'list_name': self.list_name,
            'list_closed': self.list_closed,
            'list_board_id': self.list_board_id,
            'list_subscribed': self.list_subscribed,
            'list_position': self.list_position
        }
    
    def __repr__(self):
        return '<List %s>' % self.list_name