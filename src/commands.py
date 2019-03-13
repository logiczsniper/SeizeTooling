from abc import abstractmethod, ABC
from src.constants import CommandStrings, Aesthetics, Messages
from time import time


class Command(ABC):

    def __init__(self, name, help_string, available_flags, parameter_error_msg, parameter_count, parameter_types,
                 passed_flags=None, passed_parameters=None):
        """
        Base for all commands. Saves everything required for each command to function properly, and also everything
        required in the command from the user in order for the function to be valid and hence run.

        :param name: the name of the command passed.
        :type: str

        :param help_string: the text that will be displayed to assist the user when the --h flag is passed.
        :type: str

        :param available_flags: the flags that are viable for use with this specific command.
        :type: list

        :param parameter_error_msg: the text that will be displayed to the user when there is a fault among the
        parameters that they passed.
        :type: str

        :param parameter_count: the number of required parameters for the command.
        :type: int

        :param parameter_types: the type of each parameter- not conventional types however. The types expected in this
        parameter are either "file" or "dir". These indicate whether or not the parameter must be a path to a file or a
        path to a directory.
        :type: list

        :param passed_flags: the flags that were passed by the user.
        :type: list

        :param passed_parameters: the parameters that were passed by the user.
        :type: list
        """
        self.name = name
        self.help = help_string
        self.passed_flags = passed_flags if passed_flags is not None else list()
        self.passed_parameters = passed_parameters if passed_parameters is not None else list()
        self.available_flags = available_flags
        self.parameter_error_msg = parameter_error_msg
        self.parameter_count = parameter_count
        self.parameter_types = parameter_types

        # Preparation variables saved.
        self.starting_time = None
        self.file_references = None

    @abstractmethod
    def run(self, *args):
        """
        Default run method that must be overwritten.

        :param args: must be [[parameters passed], [flags passed]].
        :type: list
        """
        self.passed_parameters = args[0]
        self.passed_flags = args[1]

    @abstractmethod
    def preparation(self):

        # Save the starting time.
        self.starting_time = time()

        # If the --s flag was passed, save the current setup. TODO
        if "--s" in self.passed_flags:
            pass

        # Save file path references data. TODO
        self.file_references = {"": []}

    @abstractmethod
    def cleanup(self):

        # If the --v flag was passed, all details must be given back to the user. TODO
        if "--v" in self.passed_flags:
            pass
        else:
            pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class SimpleCommand(Command, ABC):
    """
    Not all commands need to complete a serious task- Help, Title and Null. Those commands inherit from this
    so that they do not need to bother overriding preparation and cleanup methods.
    """

    def preparation(self):
        pass

    def cleanup(self):
        pass


class This(Command):

    def __init__(self):
        super().__init__(CommandStrings.THIS, Messages.THIS_HELP, ["--a", "--r", "--s", "--g", "--v", "--h"],
                         "This command requires one argument: the path to target directory. " + Messages.SHORT_HELP, 1,
                         ["dir"])

    def run(self, *args):
        super().run(*args)

        print(f"Params: {self.passed_parameters}")
        print(f"Flags: {self.passed_flags}")

    def preparation(self):
        pass

    def cleanup(self):
        pass


class Transfer(Command):

    def __init__(self):
        super().__init__(CommandStrings.TRANSFER, Messages.TRANSFER_HELP, ["--g", "--v", "--h"],
                         "This command requires two arguments: the path of the file to be moved and the path of the "
                         "directory to move the file to. " + Messages.SHORT_HELP, 2, ["file", "dir"])

    def run(self, *args):
        super().run(*args)
        print("TRANSFER COMMAND")

    def preparation(self):
        pass

    def cleanup(self):
        pass


class Shift(Command):

    def __init__(self):
        super().__init__(CommandStrings.SHIFT, Messages.SHIFT_HELP, ["--a", "--r", "--s", "--g", "--v", "--h"],
                         "This command requires two arguments: the path of the directory to be moved and the path of "
                         "the directory to move the directory to. " + Messages.SHORT_HELP, 2, ["dir", "dir"])

    def run(self, *args):
        super().run(*args)
        print("SHIFT COMMAND")

    def preparation(self):
        pass

    def cleanup(self):
        pass


class Help(SimpleCommand):

    def __init__(self):
        super().__init__(CommandStrings.HELP, "Help", list(), "This command requires zero arguments. " +
                         Messages.SHORT_HELP, 0, list())

    def run(self, *args):
        print(Messages.LONG_HELP)


class Title(SimpleCommand):

    def __init__(self):
        super().__init__(CommandStrings.TITLE, str(), list(), str(), 0, list())

    def run(self, *args):
        print(Aesthetics.LOGO + "\nWelcome to the ultimate file migration tool. \nTime for you to seize the "
                                "power of Seize. " + Messages.SHORT_HELP)


class Null(SimpleCommand):

    def __init__(self):
        super().__init__(str(), str(), list(), str(), 0, list())

    def run(self, *args):
        pass
