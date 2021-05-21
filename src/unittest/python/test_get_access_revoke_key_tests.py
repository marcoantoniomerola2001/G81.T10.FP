"""Test module for testing get_access_key"""
import unittest
import csv

from secure_all import AccessManager, AccessManagementException, \
    JSON_FILES_PATH, RevokeKeyJsonStore


class TestAccessManager(unittest.TestCase):
    """Test class for testing get_access_key"""

    @classmethod
    def setUpClass(cls) -> None:
        """set up class"""
        # pylint: disable=no-member
        revoke_key_store = RevokeKeyJsonStore()
        revoke_key_store.empty_store()

    def test_revoke_key_ok_1(self):
        """Correct Case: Revocation Temporal"""
        # pylint: disable=no-member
        my_manager = AccessManager()
        result = my_manager.revoke_key(JSON_FILES_PATH + "caso_correcto_1_f3.json")
        self.assertEqual(["mail1@uc3m.es", "mail2@uc3m.es"], result)

    def test_revoke_key_ok_2(self):
        """Correct Case: Revocation Final"""
        # pylint: disable=no-member
        my_manager = AccessManager()
        result = my_manager.revoke_key(JSON_FILES_PATH + "caso_correcto_2_f3.json")
        self.assertEqual(["mail1@uc3m.es", "mail2@uc3m.es"], result)

    def test_revoke_key_ok_3(self):
        """Correct Case: Reason 100 characters"""
        # pylint: disable=no-member
        revoke_key_store = RevokeKeyJsonStore()
        revoke_key_store.empty_store()
        my_manager = AccessManager()
        result = my_manager.revoke_key(JSON_FILES_PATH + "caso_correcto_3_f3.json")
        self.assertEqual(["mail1@uc3m.es", "mail2@uc3m.es"], result)

    def test_revoke_key_ok_4(self):
        """Correct Case: Reason 99 characters"""
        # pylint: disable=no-member
        revoke_key_store = RevokeKeyJsonStore()
        revoke_key_store.empty_store()
        my_manager = AccessManager()
        result = my_manager.revoke_key(JSON_FILES_PATH + "caso_correcto_4_f3.json")
        self.assertEqual(["mail1@uc3m.es", "mail2@uc3m.es"], result)

    def test_revoke_key_wrong_1(self):
        """Wrong Case: Revocation Hola"""
        # pylint: disable=no-member
        my_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_manager.revoke_key(JSON_FILES_PATH + "caso_incorrecto_1_f3.json")
        self.assertEqual("revocation invalid", c_m.exception.message)

    def test_revoke_key_wrong_2(self):
        """Wrong Case: Revocation 101 characters"""
        # pylint: disable=no-member
        my_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_manager.revoke_key(JSON_FILES_PATH + "caso_incorrecto_2_f3.json")
        self.assertEqual("reason invalid", c_m.exception.message)

    def test_revoke_key_wrong_3(self):
        """Wrong Case: Key 63 characters"""
        # pylint: disable=no-member
        my_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_manager.revoke_key(JSON_FILES_PATH + "caso_incorrecto_3_f3.json")
        self.assertEqual("key invalid", c_m.exception.message)

    def test_revoke_key_wrong_4(self):
        """Wrong Case: Key no exist"""
        # pylint: disable=no-member
        my_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            my_manager.revoke_key(JSON_FILES_PATH + "caso_incorrecto_4_f3.json")
        self.assertEqual("key is not found or is expired", c_m.exception.message)

    def test_revoke_key_wrong_5(self):
        """Wrong Case: Key no exist"""
        # pylint: disable=no-member
        my_manager = AccessManager()
        my_manager.revoke_key(JSON_FILES_PATH + "caso_correcto_1_f3.json")
        with self.assertRaises(AccessManagementException) as c_m:
            my_manager.revoke_key(JSON_FILES_PATH + "caso_incorrecto_5_f3.json")
        self.assertEqual("key was previously revoked by this method", c_m.exception.message)

    def test_parametrized_cases_tests(self):
        """Parametrized cases read from testingCases_FP3.csv"""
        my_cases = JSON_FILES_PATH + "testingCases_FP3.csv"
        with open(my_cases, newline='', encoding='utf-8') as csvfile:
            # pylint: disable=no-member
            param_test_cases = csv.DictReader(csvfile, delimiter=';')
            my_code = AccessManager()
            for row in param_test_cases:
                file_name = JSON_FILES_PATH + row["FILE"]
                print("Param:" + row['ID TEST'] + row["VALID INVALID"])
                if row["VALID INVALID"] == "VALID":
                    valor = my_code.revoke_key(file_name)
                    self.assertEqual(row["EXPECTED RESULT"], valor)
                    print("el valor: " + valor)

                else:
                    with self.assertRaises(AccessManagementException) as c_m:
                        my_code.revoke_key(file_name)
                    self.assertEqual(c_m.exception.message, row["EXPECTED RESULT"])


if __name__ == '__main__':
    unittest.main()
