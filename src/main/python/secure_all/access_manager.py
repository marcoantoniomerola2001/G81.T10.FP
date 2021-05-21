"""Module AccessManager with AccessManager Class """

from secure_all.data.access_key import AccessKey
from secure_all.data.access_request import AccessRequest
from secure_all.storage.open_door_json_store import OpenDoorJsonStore
from secure_all.storage.revoke_key_json_store import RevokeKeyJsonStore
from secure_all.data.access_open_door import AccessOpenDoor
from secure_all.data.access_revoke_key import AccessRevokeKey

import json


class AccessManager:
    """AccessManager class, manages the access to a building implementing singleton """
    #pylint: disable=too-many-arguments,no-self-use,invalid-name, too-few-public-methods
    class __AccessManager:
        """Class for providing the methods for managing the access to a building"""

        def request_access_code(self, id_card, name_surname, access_type, email_address, days):
            """ this method give access to the building"""
            my_request = AccessRequest(id_card, name_surname, access_type, email_address, days)
            my_md5 = my_request.get_md5
            my_request.store_request()
            return my_md5

        def get_access_key( self, keyfile):
            """Returns the access key for the access code & dni received in a json file"""
            my_key = AccessKey.create_key_from_file(keyfile)
            my_key.store_keys()
            return my_key.key

        def open_door(self, key):
            """Opens the door if the key is valid an it is not expired"""
            my_key = AccessKey.create_key_from_id(key)

            if my_key.is_valid():
                my_open_door = AccessOpenDoor(key)
                my_open_door.store_open_door()
                return True

        def revoke_key( self, revokekeyfile):
            """Returns the emails of a key deactivated"""
            my_revoke_key = AccessRevokeKey.create_revoke_key_from_file(revokekeyfile)
            key = my_revoke_key.key
            my_key = AccessKey.create_key_from_id(key)

            if my_key.is_valid():
                my_revoke_key.store_revoke_key()

            return my_key.notification_emails

    __instance = None

    def __new__( cls ):
        if not AccessManager.__instance:
            AccessManager.__instance = AccessManager.__AccessManager()
        return AccessManager.__instance
