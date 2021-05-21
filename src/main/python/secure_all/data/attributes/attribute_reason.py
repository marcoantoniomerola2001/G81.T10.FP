"""Class for validating the keys"""
from secure_all.data.attributes.attribute import Attribute


class Reason(Attribute):
    """Class for validating the reason with a regex"""

    # pylint: disable=too-few-public-methods
    def __init__(self, attr_value):
        self._validation_pattern = r'(.{0,100})'
        self._error_message = "reason invalid"
        self._attr_value = self._validate(attr_value)
