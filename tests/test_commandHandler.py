from unittest import TestCase

from src.command_handler import CommandHandler


class TestCommandHandler(TestCase):

    """
    In each test, an input_set is built. Each value is a list of arguments that takes the
    place of sys.argv. The idea is that each of the commands are supposed to fail. They are all invalid commands.
    Therefore, the test passes if there are no True statements inside of the results list- they should all return False.
    """

    def setUp(self):
        self.results = list()
        self.input_set = dict()
        self.test_dir = "SeizeTool\\tests\\test_directory"
        self.test_file = "SeizeTool\\tests\\test_file.txt"

    def test_title(self):
        self.input_set = {"Pass any parameter": [str(), "param"],
                          "Pass any flag": [str(), "--h"]}

    def test_this(self):
        self.input_set = {"Pass no parameters": [str(), "this"],
                          "Pass too many parameters": [str(), "this", self.test_dir, self.test_dir],
                          "Pass a valid flag - no parameter": [str(), "this", "--a"],
                          "Pass an invalid flag": [str(), "this", self.test_dir, "--q"],
                          "Pass in invalid order": [str(), "this", "--a", self.test_dir],
                          "Pass a invalid parameter": [str(), "this", "param"]}

    def test_transfer(self):
        self.input_set = {"Pass no parameters": [str(), "transfer"],
                          "Pass too many parameters": [str(), "transfer", self.test_file, self.test_dir, self.test_dir],
                          "Pass too little parameters": [str(), "transfer", self.test_file],
                          "Pass a valid flag - no parameter": [str(), "transfer", "--g"],
                          "Pass an invalid flag": [str(), "transfer", self.test_file, self.test_dir, "--q"],
                          "Pass in invalid order": [str(), "transfer", "--g", self.test_file, self.test_dir],
                          "Pass a invalid parameter": [str(), "transfer", self.test_file, "param"]}

    def test_shift(self):
        self.input_set = {"Pass no parameters": [str(), "shift"],
                          "Pass too many parameters": [str(), "shift", self.test_dir, self.test_dir, self.test_dir],
                          "Pass too little parameters": [str(), "shift", self.test_dir],
                          "Pass a valid flag - no parameter": [str(), "shift", "--a"],
                          "Pass an invalid flag": [str(), "shift", self.test_dir, self.test_dir, "--q"],
                          "Pass in invalid order": [str(), "shift", "--a", self.test_dir, self.test_dir],
                          "Pass a invalid parameter": [str(), "shift", self.test_dir, "param"]}

    def test_null(self):
        self.input_set = {"Pass a invalid command": [str(), "invalid_command"]}

    def test_help(self):
        self.input_set = {"Pass any parameters": [str(), "help", "any_parameter"],
                          "Pass any flags": [str(), "help", "--h"]}

    def tearDown(self):

        for command in self.input_set.values():
            self.command_handler = CommandHandler(command)
            self.results.append(self.command_handler.is_valid)

        if True in self.results:
            self.fail()
