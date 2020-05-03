class Member:
    """
    A classe Member contem os seguintes campos:
        user_id, user_name, user_member_type, 
        user_id_member_referrer, user_initials, 
        user_fill_name, user_url, user_status
    """
    def __init__(self, member_json):
        self.member_json = member_json

        self.user_id = None
        self.user_name = None
        self.user_member_type = None
        self.user_id_member_referrer = None
        self.user_initials = None
        self.user_full_name = None
        self.user_url = None
        self.user_status = None

        self.load()

    """
    Metodo para carregar o membro a partir de um json
    """
    def load(self):
        self.user_id = self.member_json['id']
        self.user_name = self.member_json['username']
        self.user_member_type = self.member_json['memberType']
        self.user_id_member_referrer = self.member_json['idMemberReferrer']
        self.user_initials = self.member_json['initials']
        self.user_full_name = self.member_json['fullName']
        self.user_url = self.member_json['url']
        self.user_status = self.member_json['status']

    """
    Metodo que retorna o json do membro como foi criado
    """
    def original_json(self):
        return self.member_json

    """
    Metodo que retorna o json após processamento
    """
    def json(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'user_member_type': self.user_member_type,
            'user_id_member_referrer': self.user_id_member_referrer,
            'user_initials': self.user_initials,
            'user_full_name': self.user_full_name,
            'user_url': self.user_url,
            'user_status': self.user_status
        }

    def __repr__(self):
        return '<Member %s>' % self.user_name