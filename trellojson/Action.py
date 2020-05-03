class Action:
    def __init__(self, action_json):
        self.action_json = action_json

        self.action_id = None
        self.action_card_id = None
        self.action_card_list_id = None
        self.action_card_name = None
        self.action_card_short_id = None
        self.action_card_short_link = None
        self.action_board_id = None
        self.action_board_name = None
        self.action_board_short_link = None
        self.action_list_before_id = None
        self.action_list_before_name = None
        self.action_list_after_id = None
        self.action_list_after_name = None
        self.action_type = None
        self.action_date = None
        self.action_member_creator_id = None
        self.action_member_creator_user_name = None
        self.action_member_creator_activity_blocked = None
        self.action_member_creator_full_name = None
        self.action_member_creator_member_referrer_id = None
        self.action_member_creator_initials = None
        self.action_member_creator_non_public_available = None
        
        self.load()

    def load(self):
        self.action_id = self.action_json['id']
        self.action_type = self.action_json['type']
        self.action_date = self.action_json['date']

        try:
            self.action_card_id = self.action_json['data']['card']['id']
            if self.action_type == 'updateCard':
                self.action_card_list_id = self.action_json['data']['card']['idList']
            elif self.action_type == 'createCard':
                self.action_card_list_id = self.action_json['data']['list']['id']

            self.action_card_name = self.action_json['data']['card']['name']
            self.action_card_short_id = self.action_json['data']['card']['idShort']
            self.action_card_short_link = self.action_json['data']['card']['shortLink']
        except KeyError:
            print(f'error: tag card in action_id {self.action_id}')
        
        try:
            self.action_card_id = self.action_json['data']['card']['id']
        except KeyError:
            print(f'error: tag list in action_id {self.action_id}')
        try:
            self.action_board_id = self.action_json['data']['board']['id']
            self.action_board_name = self.action_json['data']['board']['name']
            self.action_board_short_link = self.action_json['data']['board']['shortLink']
        except KeyError:
            print(f'error: tag board in action_id {self.action_id}')

        try:
            self.action_list_before_id = self.action_json['data']['card']['listBefore']['id']
            self.action_list_before_name = self.action_json['data']['card']['listBefore']['name']
        except KeyError:
            print(f'error: tag listBefore in action_id {self.action_id}')
        
        try:
            self.action_list_after_id = self.action_json['data']['listAfter']['id']
            self.action_list_after_name = self.action_json['data']['listAfter']['name']
        except KeyError:
            print(f'error: tag listAfter in action_id {self.action_id}')

        try:
            self.action_member_creator_id = self.action_json['memberCreator']['id']
            self.action_member_creator_user_name = self.action_json['memberCreator']['username']
            self.action_member_creator_activity_blocked = self.action_json['memberCreator']['activityBlocked']
            self.action_member_creator_full_name = self.action_json['memberCreator']['fullName']
            self.action_member_creator_member_referrer_id = self.action_json['memberCreator']['idMemberReferrer']
            self.action_member_creator_initials = self.action_json['memberCreator']['initials']
            self.action_member_creator_non_public_available = self.action_json['memberCreator']['nonPublicAvailable']
        except KeyError:
            print(f'error: tag memberCreator in action_id {self.action_id}')
            
        
    def original_json(self):
        return self.action_json

    def json(self):
        return {
            'action_id': self.action_id,
            'action_card_id': self.action_card_id,
            'action_card_list_id': self.action_card_list_id,
            'action_card_name': self.action_card_name,
            'action_card_short_id': self.action_card_short_id,
            'action_card_short_link': self.action_card_short_link,
            'action_board_id': self.action_board_id,
            'action_board_name': self.action_board_name,
            'action_board_short_link': self.action_board_short_link,
            'action_list_before_id': self.action_list_before_id,
            'action_list_before_name': self.action_list_before_name,
            'action_list_after_id': self.action_list_after_id,
            'action_list_after_name': self.action_list_after_name,
            'action_type': self.action_type,
            'action_date': self.action_date,
            'action_member_creator_id': self.action_member_creator_id,
            'action_member_creator_user_name': self.action_member_creator_user_name,
            'action_member_creator_activity_blocked': self.action_member_creator_activity_blocked,
            'action_member_creator_full_name': self.action_member_creator_full_name,
            'action_member_creator_member_referrer_id': self.action_member_creator_member_referrer_id,
            'action_member_creator_initials': self.action_member_creator_initials,
            'action_member_creator_non_public_available': self.action_member_creator_non_public_available
        }
    
    def __repr__(self):
        return '<Action %s>' % self.action_type