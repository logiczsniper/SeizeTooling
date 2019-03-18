from os import path

from src.commands import This, Shift, Transfer, Help, Title, Null
from src.constants import CommandStrings, Messages


class CommandChecker:

    def __init__(self, sys_argv):

        # Save all input
        self.all_input = sys_argv

        # Test if blank command
        if len(self.all_input) == 1:
            # append a blank to all input so it does not raise an error- this is a valid command!
            self.all_input.append("")

        # Create the command
        self.command = self.create_command(self.all_input[1])

        # Analysing the flags.
        self.all_flags = [arg for arg in self.all_input if arg in ["--a", "--r", "--s", "--g", "--h", "--v"]]
        self.applicable_flags = list(set(self.all_flags) & set(self.command.available_flags))
        self.invalid_flags = [arg for arg in self.all_input if "--" in arg and arg not in self.command.available_flags]

        # Save the parameters
        self.parameters = [arg for arg in self.all_input if "--" not in arg and
                           arg not in [self.all_input[0], self.all_input[1]]]

        # Assert whether or not the command is valid
        self.is_valid = True
        if not self.check_command() or not self.check_parameters() or not self.check_flags() or not self.check_order():
            self.is_valid = False

    @staticmethod
    def create_command(command_string: str):
        if command_string == CommandStrings.TITLE:
            command = Title()
        elif command_string == CommandStrings.THIS:
            command = This()
        elif command_string == CommandStrings.TRANSFER:
            command = Transfer()
        elif command_string == CommandStrings.SHIFT:
            command = Shift()
        elif command_string == CommandStrings.HELP:
            command = Help()
        else:
            command = Null()

        return command

    @property
    def seize_script_path(self) -> str:

        if self.is_valid:
            return self.all_input[0]

    @property
    def args(self):

        if self.is_valid:
            return self.all_input[2::]

    def check_command(self) -> bool:

        # If a command was given but it is not one of the available commands, take action.
        if isinstance(self.command, Null):
            print("Command was not valid. " + Messages.SHORT_HELP)
            return False

        return True

    def check_parameters(self) -> bool:

        # Parameters are only required if there is no --h flag
        if "--h" not in self.all_flags:

            # If no parameters are provided and the command is not 'help' or 'title' or 'null', take action.
            if self.all_input[2::] == list() and not isinstance(self.command, (Help, Title, Null)):
                print("No parameters provided. " + Messages.SHORT_HELP)
                return False

            # If the wrong number of parameters are provided, take action.
            elif self.command.parameter_count != len(self.parameters):
                print(self.command.parameter_error_msg)
                return False

            # Check that the parameters are valid directory or file paths
            else:
                for index, path_type in enumerate(self.command.parameter_types):
                    if path_type == "file" and not path.isfile(self.parameters[index]):
                        print(f"Invalid parameter: {self.parameters[index]}. Must be a file path. " +
                              Messages.SHORT_HELP)
                        return False
                    elif path_type == "dir" and not path.isdir(self.parameters[index]):
                        print(f"Invalid parameter: {self.parameters[index]}. Must be a directory path. " +
                              Messages.SHORT_HELP)
                        return False

        return True

    def check_flags(self) -> bool:

        # If invalid flags were present in the input, take action.
        if self.invalid_flags != list():
            print(f"Invalid flag(s): {self.invalid_flags}. " + Messages.SHORT_HELP)
            return False

        # If help was requested, return false and print the relevant command's help message.
        elif "--h" in self.all_flags:
            print(self.command.help)
            return False

        return True

    def check_order(self) -> bool:

        # Assuming the command comes first, check that what follows is the parameter(s) then the flag(s).
        flag_found = False
        for arg in self.all_input:
            if self.all_input.index(arg) in [0, 1]:
                continue

            if arg in self.all_flags:
                flag_found = True

            if flag_found and arg not in self.all_flags:
                print("Invalid order in command. " + Messages.SHORT_HELP)
                return False

        return True
