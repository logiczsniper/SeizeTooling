from abc import abstractmethod, ABC
from src.constants import CommandStrings, Aesthetics, Messages


class Command(ABC):

    def __init__(self, name, help_string, available_flags, parameter_error_msg, parameter_count, parameter_types,
                 passed_flags=None, passed_parameters=None):
        self.name = name
        self.help = help_string
        self.passed_flags = passed_flags if passed_flags is not None else list()
        self.passed_parameters = passed_parameters if passed_parameters is not None else list()
        self.available_flags = available_flags
        self.parameter_error_msg = parameter_error_msg
        self.parameter_count = parameter_count
        self.parameter_types = parameter_types

    @abstractmethod
    def run(self, *args):
        """
        Default run method that must be overwritten.

        :param args: must be [[parameters passed], [flags passed]].
        :type: list
        """
        self.passed_parameters = args[0]
        self.passed_flags = args[1]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class This(Command):

    def __init__(self):
        super().__init__(CommandStrings.THIS, Messages.THIS_HELP, ["--a", "--r", "--s", "--g", "--v", "--h"],
                         "This command requires one argument: the path to target directory. " + Messages.SHORT_HELP, 1,
                         ["dir"])

    def run(self, *args):
        super().run(*args)

        print(f"Params: {self.passed_parameters}")
        print(f"Flags: {self.passed_flags}")


class Transfer(Command):

    def __init__(self):
        super().__init__(CommandStrings.TRANSFER, Messages.TRANSFER_HELP, ["--g", "--v", "--h"],
                         "This command requires two arguments: the path of the file to be moved and the path of the "
                         "directory to move the file to. " + Messages.SHORT_HELP, 2, ["file", "dir"])

    def run(self, *args):
        print("TRANSFER COMMAND")


class Shift(Command):

    def __init__(self):
        super().__init__(CommandStrings.SHIFT, Messages.SHIFT_HELP, ["--a", "--r", "--s", "--g", "--v", "--h"],
                         "This command requires two arguments: the path of the directory to be moved and the path of "
                         "the directory to move the directory to. " + Messages.SHORT_HELP, 2, ["dir", "dir"])

    def run(self, *args):
        print("SHIFT COMMAND")


class Help(Command):

    def __init__(self):
        super().__init__(CommandStrings.SHIFT, "Help", list(), "This command requires zero arguments. " +
                         Messages.SHORT_HELP, 0, list())

    def run(self, *args):

        print(Messages.LONG_HELP)


class Title(Command):

    def __init__(self):
        super().__init__(CommandStrings.TITLE, str(), list(), str(), 0, list())

    def run(self, *args):
        print(Aesthetics.LOGO + "\nWelcome to the ultimate file migration tool. \nTime for you to seize the "
                                "power of Seize. " + Messages.SHORT_HELP)


class Null(Command):

    def __init__(self):
        super().__init__(str(), str(), list(), str(), 0, list())

    def run(self, *args):
        pass
