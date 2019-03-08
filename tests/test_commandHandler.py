from unittest import TestCase
from src.command_handler import CommandHandler
import sys
import io


class TestCommandHandler(TestCase):

    def setUp(self):
        self.old_stdout = sys.stdout
        sys.stdout = self.buffer = io.StringIO()
        self.expected_output = str()

        self.command_handler = CommandHandler(sys.argv)

    def test_create_command(self):
        self.expected_output = ""

    def test_check_parameters(self):
        self.expected_output = ""

    def test_check_command(self):
        self.expected_output = ""

    def test_check_flags(self):
        self.expected_output = ""

    def tearDown(self):
        sys.stdout = self.old_stdout
        if self.expected_output != self.buffer.getvalue():
            self.fail()
