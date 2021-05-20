"""Test module for testing get_access_key"""
import unittest
import csv

from secure_all import AccessManager, AccessManagementException, \
    JSON_FILES_PATH, KeysJsonStore, RequestJsonStore


class TestAccessManager(unittest.TestCase):
    """Test class for testing get_access_key"""


    @classmethod
    def setUpClass(cls) -> None:
        """"""
        # pylint: disable=no-member

        revoke_key_store = RevokeKeyJsonStore()
        revoke_key_store.empty_store()

        # introduce a key valid and not expired and guest
        my_manager = AccessManager()
        print("one")
        my_manager.revoke_key(JSON_FILES_PATH + "caso_correcto_f3.json")

        print("Finished init")


    def test_parametrized_cases_tests( self ):
        """Parametrized cases read from testingCases_RF1.csv"""
        my_cases = JSON_FILES_PATH + "testingCases_FP3.csv"
        with open(my_cases, newline='', encoding='utf-8') as csvfile:
            #pylint: disable=no-member
            param_test_cases = csv.DictReader(csvfile, delimiter=';')
            my_code = AccessManager()
            for row in param_test_cases:
                file_name = JSON_FILES_PATH + row["FILE"]
                print("Param:" + row[ 'ID TEST' ] + row["VALID INVALID"])
                if row["VALID INVALID"] ==  "VALID":
                    valor = my_code.revoke_key(file_name)
                    self.assertEqual(row[ "EXPECTED RESULT" ], valor)
                    print("el valor: " + valor)

                else:
                    with self.assertRaises(AccessManagementException) as c_m:
                        my_code.revoke_key(file_name)
                    self.assertEqual(c_m.exception.message, row[ "EXPECTED RESULT" ])

if __name__ == '__main__':
    unittest.main()
