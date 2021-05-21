"""Implements the RequestsJSON Store"""
from secure_all.storage.json_store import JsonStore
from secure_all.cfg.access_manager_config import JSON_FILES_PATH


class OpenDoorJsonStore:
    """Extends JsonStore"""

    class __OpenDoorJsonStore(JsonStore):
        # pylint: disable=invalid-name

        ID_FIELD = '_AccessOpenDoor__key'
        OPEN_DOOR__TIME = '_AccessOpenDoor__time'

        _FILE_PATH = JSON_FILES_PATH + "storeOpenDoor.json"
        _ID_FIELD = ID_FIELD

    __instance = None

    def __new__(cls):
        if not OpenDoorJsonStore.__instance:
            OpenDoorJsonStore.__instance = OpenDoorJsonStore.__OpenDoorJsonStore()
        return OpenDoorJsonStore.__instance

    def __getattr__(self, name):
        return getattr(self.__instance, name)

    def __setattr__(self, name, valor):
        return setattr(self.__instance, name, valor)
