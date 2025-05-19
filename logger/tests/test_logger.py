import unittest
import tempfile
import os
import logging
from io import StringIO
from contextlib import redirect_stdout

from .. import Logger  # Adjust import if needed


class TestLogger(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # Reset singleton before all tests
        Logger.__instance = None

        # Create temp files for logs
        cls.info_log = tempfile.NamedTemporaryFile(delete=False)
        cls.crit_log = tempfile.NamedTemporaryFile(delete=False)
        cls.info_path = cls.info_log.name
        cls.crit_path = cls.crit_log.name
        cls.info_log.close()
        cls.crit_log.close()

        # Load the logger once
        logger = Logger.get_instance()
        logger.load_logger(
            app_name="TestApp",
            critical_file=cls.crit_path,
            info_file=cls.info_path,
            files_max_size=1,
            backup_count=1,
            console=True,
            level=logging.DEBUG
        )

    @classmethod
    def tearDownClass(cls):
        # Clean up files after all tests
        os.remove(cls.info_path)
        os.remove(cls.crit_path)
        Logger.__instance = None

    def test_logger_load_and_file_logging(self):
        # Test the singleton nature
        logger1 = Logger.get_instance()
        logger2 = Logger.get_instance()
        self.assertIs(logger1, logger2)

        # Write messages in the tests
        Logger.debug("Debug message")
        Logger.info("Info message")
        Logger.warning("Warning message")
        Logger.error("Error message")
        Logger.critical("Critical message")

        # Check messages in log file
        with open(self.info_path, 'r', encoding='utf-8') as f:
            info_logs = f.read()
            self.assertIn("Info message", info_logs)
            self.assertIn("Warning message", info_logs)

        # Check messages in crit file
        with open(self.crit_path, 'r', encoding='utf-8') as f:
            crit_logs = f.read()
            self.assertIn("Error message", crit_logs)
            self.assertIn("Critical message", crit_logs)
        
        # Console is not tested
        # TODO Test the console output
        
if __name__ == '__main__':
    unittest.main()
