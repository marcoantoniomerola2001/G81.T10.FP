"""Implements the RequestsJSON Store"""
from secure_all.storage.json_store import JsonStore
from secure_all.exception.access_management_exception import AccessManagementException
from secure_all.cfg.access_manager_config import JSON_FILES_PATH


class OpenDoorJsonStore():
    """Extends JsonStore"""

    class __OpenDoorJsonStore(JsonStore):
        # pylint: disable=invalid-name
        INVALID_ITEM = "Invalid item to be stored as a request"
        ID_ALREADY_STORED = "key already found in storeRequest"
        NOT_FOUND_IN_THE_STORE = "key does not match"

        ID_FIELD = '_AccessOpenDoor__key'
        OPEN_DOOR__TIME = '_AccessOpenDoor__time'

        _FILE_PATH = JSON_FILES_PATH + "storeOpenDoor.json"
        _ID_FIELD = ID_FIELD

        def add_item(self, item):
            """add item to the json"""
            #pylint: disable=import-outside-toplevel,cyclic-import
            from secure_all.data.access_open_door import AccessOpenDoor

            if not isinstance(item, AccessOpenDoor):
                raise AccessManagementException(self.INVALID_ITEM)
            if not self.find_item(item.key) is None:
                raise AccessManagementException(self.ID_ALREADY_STORED)

            return super().add_item(item)

    __instance = None

    def __new__(cls):
        if not OpenDoorJsonStore.__instance:
            OpenDoorJsonStore.__instance = OpenDoorJsonStore.__OpenDoorJsonStore()
        return OpenDoorJsonStore.__instance

    def __getattr__ (self, nombre ):
        return getattr(self.__instance, nombre)

    def __setattr__ ( self, nombre, valor ):
        return setattr(self.__instance, nombre, valor)