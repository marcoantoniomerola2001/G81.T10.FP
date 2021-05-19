

class AccessOpenDoor:

    def __init__(self, key, time):
        self.__key = key
        self.__time = time

    @property
    def key( self ):
        """getter key"""
        return self.__key
    @key.setter
    def key(self, value):
        """setter key"""
        self.__key = value

    @property
    def time( self ):
        """getter key"""
        return self.__time
    @time.setter
    def time(self, value):
        """setter key"""
        self.__time = value