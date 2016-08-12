"""
Test creation of duplicated vocabularies.
"""

import os
import shutil
import unittest

from tests import VocabConfig


class TestCreateDuplicatedVocabulary(unittest.TestCase, VocabConfig):
    def setUp(self):
        # subprocess.check_call(['su', '-', 'irods'])
        self.call_irm_vocab()

        if os.path.exists(self.VOCAB_DIR):
            shutil.rmtree(self.VOCAB_DIR)

        self.call_create_vocab_rule(
            path=self.IRODS_TEST_COLL_ABS_PATH,
            resc=self.IRODS_TEST_RESC,
            vocab_name=self.TEST_VOCAB_NAME,
            vocab_author=self.TEST_VOCAB_AUTHOR
        )

    def test_create_duplicated_vocab(self):
        """
        mlxCreateVocabulary rule should throw an error when adding a vocabulary to a collection that already has one.
        """

        self.assertTrue(self.call_create_vocab_rule(
            path=self.IRODS_TEST_COLL_ABS_PATH,
            resc=self.IRODS_TEST_RESC,
            vocab_name=self.TEST_VOCAB_NAME,
            vocab_author=self.TEST_VOCAB_AUTHOR
        ) != 0)

    def tearDown(self):
        self.rm_rf_vocab_file()


if __name__ == '__main__':
    unittest.main()
