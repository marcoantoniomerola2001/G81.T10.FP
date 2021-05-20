"""Implements the RequestsJSON Store"""
from secure_all.storage.json_store import JsonStore
from secure_all.exception.access_management_exception import AccessManagementException
from secure_all.cfg.access_manager_config import JSON_FILES_PATH


class RevokeKeyJsonStore():
    """Extends JsonStore"""

    class __RevokeKeyJsonStore(JsonStore):
        # pylint: disable=invalid-name
        ID_FIELD = '_AccessRevokeKey__key'
        REVOKE_KEY__REVOCATION = '_AccessRevokeKey__revocation'
        REVOKE_KEY__REASON = '_AccessRevokeKey__reason'

        _FILE_PATH = JSON_FILES_PATH + "storeRevokeKeys.json"
        _ID_FIELD = ID_FIELD

        def add_item( self, item):
            """Implementing the restrictions related to avoid duplicated keys"""
            #pylint: disable=import-outside-toplevel,cyclic-import
            from secure_all.data.access_revoke_key import AccessRevokeKey

            if not isinstance(item,AccessRevokeKey):
                raise AccessManagementException("invalid item to be stored as a revoke_key")

            if not self.find_item(item.key) is None:
                raise AccessManagementException("key was previously revoked by this method")

            return super().add_item(item)

    __instance = None

    def __new__(cls):
        if not RevokeKeyJsonStore.__instance:
            RevokeKeyJsonStore.__instance = RevokeKeyJsonStore.__RevokeKeyJsonStore()
        return RevokeKeyJsonStore.__instance

    def __getattr__ (self, nombre ):
        return getattr(self.__instance, nombre)

    def __setattr__ ( self, nombre, valor ):
        return setattr(self.__instance, nombre, valor)