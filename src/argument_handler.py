from src.constants import CommandStrings, Aesthetics


class ArgumentHandler:

    def __init__(self, sys_argv):
        self.all_args = sys_argv
        self.isValid = False if self.check_args() is False else True
        self.flags = [arg for arg in sys_argv if arg in ["--a", "--r", "--s", "--g", "--h"]]

    @property
    def seize_script_path(self):

        if self.isValid:
            return self.all_args[0]

    @property
    def command(self):

        if self.isValid:
            return self.all_args[1]

    @property
    def args(self):

        if self.isValid:
            return self.all_args[2::]

    def check_args(self):

        # If no args are given (besides the path), welcome the user. This is however not valid in terms of creating a
        # seize command.
        if len(self.all_args) == 1:
            print(
                Aesthetics.LOGO + "\nWelcome to the ultimate file migration tool. \nTime for you to seize the "
                                  "power of Seize. Use --h for available commands and flags.\n\n")
            return False

        # Check if the command was valid and arguments were provided.
        else:
            if self.all_args[1] not in [CommandStrings.THIS, CommandStrings.SHIFT, CommandStrings.TRANSFER]:
                print("Command was not valid. Use --h for available commands and flags.")
                return False
            if self.all_args[2::] == list():
                print("No arguments provided. Use --h for available commands and flags.")
                return False
            # TODO make changes so that you can tell the user if all of the flags are valid.

        # TODO depending on the command, check that the appropriate arguments were provided.
