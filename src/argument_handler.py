from src.commands import This, Shift, Transfer
from src.constants import CommandStrings, Aesthetics


class ArgumentHandler:

    def __init__(self, sys_argv):

        self.all_args = [arg for arg in sys_argv if "--" not in arg]
        self.flags = [arg for arg in sys_argv if arg in ["--a", "--r", "--s", "--g", "--h"]]
        self.invalid_flags = [arg for arg in sys_argv if "--" in arg and arg not in self.flags]
        self.parameters = [arg for arg in sys_argv if arg not in self.flags and arg not in [sys_argv[0], sys_argv[1]]]

        self.isValid = False if self.check_args() is False else True

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
                                  "power of Seize. Use 'seize help' for assistance.\n\n")
            return False

        # If help was requested, return false and print the relevant command's help message.
        elif "--h" in self.flags:

            if self.all_args[1] == CommandStrings.THIS:
                new_this = This()
                print(new_this.help)

            elif self.all_args[1] == CommandStrings.SHIFT:
                new_shift = Shift()
                print(new_shift.help)

            elif self.all_args[1] == CommandStrings.TRANSFER:
                new_transfer = Transfer()
                print(new_transfer.help)

            return False

        # Check if the command was valid and arguments were provided.
        else:
            if self.all_args[1] not in [CommandStrings.THIS, CommandStrings.SHIFT, CommandStrings.TRANSFER,
                                        CommandStrings.HELP]:
                print("Command was not valid. Use 'seize help' for assistance.")
                return False
            if self.all_args[2::] == list() and self.all_args[1] != CommandStrings.HELP:
                print("No arguments provided. Use 'seize help' for assistance.")
                return False
            if self.invalid_flags != list():
                print(f"Invalid flag(s): {self.invalid_flags}. Use 'seize help' for assistance.")
                return False
            if self.all_args[1] == CommandStrings.THIS and len(self.parameters) != 1:
                print(
                    "This command requires one argument: the path to target directory. Use 'seize help' for assistance")
                return False
