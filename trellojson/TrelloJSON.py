import json
import os

from Member import Member
from List import List
from Card import Card
from Action import Action

# https://webapps.stackexchange.com/questions/47272/how-to-construct-url-of-trello-json-download-from-board-url-without-using-the-a
# https://codebeautify.org/jsonviewer
# https://regex101.com/

class TrelloJson():
    def __init__(self):
        self.file_path = None
        self._json_data = None
        
        self.board_id = None
        self.board_name = None
        self.board_url = None

        self._cards = None
        self._members = None
        self._lists = None
        self._labels = None
        self._actions = None
        self._cards_json = None
        self._members_json = None
        self._lists_json = None
        self._labels_json = None
        self._actions_json = None
        
    """
    Metodo para carregar o json
    Parametros: 
        file_path: Caminho do arquivo
        json_data: Dados em formato json(dict)
    """
    def load(self, file_path= None, json_data=None):
        if file_path:
            self.file_path = file_path 
            self._json_data = self.read_file_from_json()
        elif json_data:
            self._json_data = json.loads(json_data)

        if self._json_data:
            self.board_id = self._json_data["id"]
            self.board_name = self._json_data["name"]
            self.board_url = self._json_data["url"]
            
            self._cards_json = self._json_data["cards"]
            self._members_json = self._json_data["members"]
            self._lists_json = self._json_data["lists"]
            self._labels_json = self._json_data["labelNames"]
            self._actions_json = self._json_data["actions"]

    def read_file_from_json(self):
        with open(self.file_path, encoding="utf8") as jsonFile:
            data = json.loads(jsonFile.read())
            return data
        return None

    def json(self):
        return self._json_data
    
    @property
    def list_lists(self):
        if self._lists:
            return self._lists
        else:
            self._lists = []
            for list_json in self._lists_json:
                self._lists.append(List(list_json))
                
            return self._lists

    @property
    def list_cards(self):
        if self._cards:
            return self._cards
        else:
            self._cards = []
            for card_json in self._cards_json:
                self._cards.append(Card(card_json))
            
            return self._cards
    
    """
    Metodo para retornar em uma lista json os dados de uma list de objetos do package trellojson.
    A chave para acessar os dados e 'data'
    """
    def convert_to_json(self, list_object):
        return {"data": [obj.json() for obj in list_object]}
    
    @property
    def list_members(self):
        if self._members:
            return self._members
        else:
            self._members = []
            for member_json in self._members_json:
                self._members.append(Member(member_json))
            return self._members
        
    @property
    def list_labels(self):
        if self._labels:
            return self._labels
        else:
            self._labels = self._labels_json
            return self._labels
    
    @property
    def list_actions(self):
        if self._actions:
            return self._actions
        else:
            self._actions = []
            for action_json in self._actions_json:
                self._actions.append(Action(action_json))
            return self._actions


    def list_by_id(self, list_id):
        for it in self._lists:
            if it.list_id == list_id:
                return it
        return None

    def card_by_id(self, card_id):
        for it in self._cards:
            if it.card_id == card_id:
                return it
        return None
    
    def member_by_id(self, member_id):
        for it in self._members:
            if it.user_id == member_id:
                return it
        return None
    
    def action_by_id(self, action_id):
        if not self._actions:
            self.list_actions
        
        for it in self._actions:
            if it.action_id == action_id:
                return it
        return None
    
    def actions_by_member_creator_id(self, member_creator_id):
        if not self._actions:
            self.list_actions
        
        actions = [it for it in self._actions if it.action_member_creator_id == member_creator_id]
        return actions

    def actions_by_type(self, action_type):
        if not self._actions:
            self.list_actions
        
        actions = [it for it in self._actions if it.action_type == action_type]
        return actions
        
if __name__ == "__main__":

    file_name = os.path.join(os.path.join(os.getcwd(), 'trellojson'), 'ZaO76oET.json')
    
    trello_json = TrelloJson()
    trello_json.load(file_name)
    

    
    #members = trello_json.list_members
    #print(members)

    #lists = trello_json.list_lists
    #print(lists)
    
    #cards = trello_json.list_cards
    #print(cards)

    #labels = trello_json.list_labels
    #print(labels)

    #actions = trello_json.actions_by_type('createCard')
    #print(actions)
