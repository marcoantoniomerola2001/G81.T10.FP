"""Class for parsing input JSON Files for the secure_all system"""
import json
from secure_all.exception.access_management_exception import AccessManagementException


class JsonParser:
    """Class for parsing input JSON Files for the secure_all system"""
    # pylint: disable=too-few-public-methods
    _key_list = []
    _key_error_message = "JSON Decode Error - Wrong label"
    ERROR_FORMAT = "JSON Decode Error - Wrong JSON Format"
    WRONG_PATH = "Wrong file or file path"

    def __init__(self, file):
        self._file = file
        self._json_content = self._parse_json_file()
        self._validate_json()

    def _parse_json_file(self):
        """read the file in json format format"""
        try:
            with open(self._file, "r", encoding="utf-8", newline="") as json_file:
                data = json.load(json_file)
        except FileNotFoundError as ex:
            raise AccessManagementException(self.WRONG_PATH) from ex
        except json.JSONDecodeError as ex:
            raise AccessManagementException(self.ERROR_FORMAT) from ex
        return data

    def _validate_json(self):
        """validate the json keys"""
        for key in self._key_list:
            if key not in self._json_content.keys():
                raise AccessManagementException(self._key_error_message)

    @property
    def json_content(self):
        """Property for access the json content read from the json file"""
        return self._json_content
