from secure_all.parser.revoke_key_json_parser import RevokeKeyJsonParser
from secure_all.data.attributes.attribute_key import Key
from secure_all.data.attributes.attribute_revocation import Revocation
from secure_all.data.attributes.attribute_reason import Reason
from secure_all.storage.revoke_key_json_store import RevokeKeyJsonStore

class AccessRevokeKey:

    def __init__(self, key, revocation, reason):
        self.__key = Key(key).value
        self.__revocation = Revocation(revocation).value
        self.__reason = Reason(reason).value

    @property
    def key( self ):
        """getter key"""
        return self.__key
    @key.setter
    def key(self, value):
        """setter key"""
        self.__key = value

    @property
    def revocation( self ):
        """getter revocation"""
        return self.__revocation
    @revocation.setter
    def revocation(self, value):
        """setter key"""
        self.__revocation = value

    @property
    def reason( self ):
        """getter reason"""
        return self.__reason
    @revocation.setter
    def reason(self, value):
        """setter reason"""
        self.__reason = value

    @classmethod
    def create_revoke_key_from_file(cls, revoke_key_file):
        """Class method from creating an instance of AccessRevokeKey
        from the content of a file according to FP3"""
        access_revoke_key_items = RevokeKeyJsonParser(revoke_key_file).json_content
        return cls(access_revoke_key_items[RevokeKeyJsonParser.KEY],
                   access_revoke_key_items[RevokeKeyJsonParser.REVOCATION],
                   access_revoke_key_items[RevokeKeyJsonParser.REASON])

    def store_revoke_key(self):
        """Storing revoke key"""

        storejson = RevokeKeyJsonStore()
        storejson.add_item(self)

