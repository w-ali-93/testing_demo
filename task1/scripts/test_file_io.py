import unittest
from unittest.mock import patch
import filecmp, os, shutil, sys, io, pathlib
from file_io import fileIO


class FileIOTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
            Defines common variables for the FileIOTestCase methods.
        """
        try:
            cls._base_path = str(pathlib.Path(__file__).parent.absolute())
            cls._temp_dir_path = cls._base_path + r'/tests/unit/output/temp/'
            cls._golden_ref_path = cls._base_path \
                + r'/tests/unit/golden_ref/file_io/'

        except Exception as e:
            raise("Testcase class setup failed: " + str(e))


    def setUp(self):
        """
            Sets up the environment for unit testing the methods present
            in the 'file_io.py' module.
        """
        try:
            if os.path.exists(self._temp_dir_path):
                shutil.rmtree(self._temp_dir_path) 
            os.mkdir(self._temp_dir_path)

        except Exception as e:
            raise("Testcase setup failed: " + str(e))

    
    def test_write_ints_to_file_valid(self):
        """
            Executes the 'write_ints_to_file' method with arguments
            that should yield correct output. Compares written file
            against Golden reference. Fails if output file does not
            exist or if comparison returns False.
        """
        test_file_io_object = fileIO(self._temp_dir_path + r'res.txt')
        test_file_io_object.write_ints_to_file(1, 100)

        self.assertTrue(os.path.exists(self._temp_dir_path + r'res.txt'), \
                'FAILURE: output of ' \
                + test_file_io_object.write_ints_to_file.__name__ \
                + ' does not exist on disk.')

        self.assertTrue(filecmp.cmp(self._temp_dir_path + r'res.txt', \
                self._golden_ref_path + r'write_ints_to_file/valid.txt'), \
                'FAILURE: output of ' \
                + test_file_io_object.write_ints_to_file.__name__ \
                + ' does not match Golden reference.')

    
    def test_read_half_ints_in_file_valid(self):
        """
            Executes the 'read_half_ints_in_file' method with arguments
            that should give correct output. Compares console output
            against the string representation of a Python list
            containing integers from 1 through 50. Fails if comparison
            fails.
        """
        capturedOutput = io.StringIO()
        refOutput = str(list(range(1, 51)))

        sys.stdout = capturedOutput
        test_file_io_object = fileIO(self._golden_ref_path \
            + r'read_half_ints_in_file/valid.txt')
        test_file_io_object.read_half_ints_in_file()
        sys.stdout = sys.__stdout__

        self.assertEqual(capturedOutput.getvalue().strip(), refOutput, \
                'FAILURE: actual output of ' \
                + test_file_io_object.read_half_ints_in_file.__name__ \
                + ' does not match expected output.')


    @patch.object(fileIO, 'read_half_ints_in_file')
    @patch.object(fileIO, 'write_ints_to_file')
    def test_write_ints_then_read_half(self, mockwrite_ints_to_file, \
        mockread_half_ints_in_file):
        """
            Executes the '_write_ints_then_read_half' method and checks
            that exactly one call to 'write_ints_to_file' is made with
            valid parameters and exactly one call to
            'read_half_ints_in_file' is made.
        """
        test_file_io_object = fileIO(self._temp_dir_path + r'res.txt')
        test_file_io_object.write_ints_then_read_half()

        mockwrite_ints_to_file.assert_called_once_with(1, 100)
        mockread_half_ints_in_file.assert_called_once()

    
    def tearDown(self):
        """
            Tears down for TestFileIOMethods unit tests.
        """
        try:
            shutil.rmtree(self._temp_dir_path)

        except Exception as e:
            raise("Testcase teardown failed: " + str(e))


def test_suite():
    testSuite = unittest.TestSuite()
    testSuite.addTest(FileIOTestCase('test_write_ints_to_file_valid'))
    testSuite.addTest(FileIOTestCase('test_read_half_ints_in_file_valid'))
    testSuite.addTest(FileIOTestCase('test_write_ints_then_read_half'))
    return testSuite


if __name__ == '__main__':
    testRunner = unittest.TextTestRunner()
    testRunner.run(test_suite())
