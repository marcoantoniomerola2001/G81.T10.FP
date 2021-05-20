"""parser for input key files according to FP3"""

from secure_all.parser.json_parser import JsonParser

class RevokeKeyJsonParser(JsonParser):
    """parser for revoke key"""
    #pylint: disable=too-few-public-methods
    KEY = "Key"
    REVOCATION = "Revocation"
    REASON = "Reason"
    _key_list = [KEY, REVOCATION, REASON]