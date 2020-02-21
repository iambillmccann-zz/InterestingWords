from unittest import TestCase
from modules import utilities

class utilities_test(TestCase):

    def number_of_files(self):

        actual_number_of_files = 6  # This is a hardcoded value based on provided data
        expected_number_of_files = utilities.get_file_names("./corpus").__len__

        self.assertTrue(expected_number_of_files == actual_number_of_files)