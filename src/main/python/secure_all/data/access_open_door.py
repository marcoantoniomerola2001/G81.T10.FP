"""imports"""
from datetime import datetime
from secure_all.storage.open_door_json_store import OpenDoorJsonStore


class AccessOpenDoor:
    """class for AcessOpenDoor"""

    def __init__(self, key):
        self.__key = key
        self.__time = datetime.timestamp(datetime.utcnow())

    @property
    def key(self):
        """getter key"""
        return self.__key

    @key.setter
    def key(self, value):
        """setter key"""
        self.__key = value

    @property
    def time(self):
        """getter key"""
        return self.__time

    @time.setter
    def time(self, value):
        """setter key"""
        self.__time = value

    def store_open_door(self):
        """Storing open door"""
        open_door_store = OpenDoorJsonStore()
        open_door_store.add_item(self)
