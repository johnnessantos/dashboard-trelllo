import os
import sys
import unittest

sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), 'trellojson'))

from Action import Action
from TrelloJSON import TrelloJson

class TestAction(unittest.TestCase):

    def test_list_actions(self):
        file_name = os.path.join(os.path.join(os.getcwd(), 'trellojson'), 'ZaO76oET.json')
        trello_json = TrelloJson()
        trello_json.load(file_path=file_name)
        actions = trello_json.list_actions

        assert type(actions) == list
        assert len(actions) == 16

    def test_list_actions_by_id(self):
        file_name = os.path.join(os.path.join(os.getcwd(), 'trellojson'), 'ZaO76oET.json')
        trello_json = TrelloJson()
        trello_json.load(file_path=file_name)
        action = trello_json.action_by_id('5e650e700a3a3120fe957960')
        
        assert action != None


if __name__ == "__main__":
    unittest.main()