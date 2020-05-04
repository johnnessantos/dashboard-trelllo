from datetime import datetime

class Card:
    def __init__(self, card_json):
        self.card_json = card_json

        self.card_id  = None
        self.card_name = None
        self.card_date_last_activity = None
        self.card_board_id = None
        self.card_labels_id = None
        self.card_list_id = None
        self.card_members_id = None
        self.card_labels = None
        self.card_short_id = None
        self.card_short_link = None
        self.subscribed = None
        self.card_url = None
        self.card_position = None

        self.load()

    def load(self):
        self.card_id  = self.card_json['id']
        self.card_name = self.card_json['name']
        self.card_date_last_activity = self.card_json['dateLastActivity']
        self.card_board_id = self.card_json['idBoard']
        self.card_labels_id = self.card_json['idLabels'] #json
        self.card_list_id = self.card_json['idList'] 
        self.card_members_id = self.card_json['idMembers'] #json
        self.card_labels = self.card_json['labels'] #json
        self.card_short_id = self.card_json['idShort']
        self.card_short_link = self.card_json['shortLink']
        self.subscribed = self.card_json['subscribed']
        self.card_url = self.card_json['url']
        self.card_position = self.card_json['pos']

        # Converting javascript datetime zone
        self.card_date_last_activity = datetime.strptime(self.card_date_last_activity, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.card_date_last_activity = self.card_date_last_activity.strftime('%d/%m/%Y %H:%M:%S')


    def original_json(self):
        return self.card_json

    def json(self):
        return {
            'card_id ': self.card_id ,
            'card_name': self.card_name,
            'card_date_last_activity': self.card_date_last_activity,
            'card_board_id': self.card_board_id,
            'card_labels_id': self.card_labels,
            'card_list_id': self.card_list_id,
            'card_members_id': self.card_members_id,
            'card_labels': self.card_labels,
            'card_short_id': self.card_short_id,
            'card_short_link': self.card_short_link,
            'subscribed': self.subscribed,
            'card_url': self.card_url,
            'card_position': self.card_position
        }
        
    def __repr__(self):
        return '<card %s>' % self.card_name