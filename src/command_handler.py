from src.commands import This, Shift, Transfer, Help
from src.constants import CommandStrings, Aesthetics


class CommandHandler:

    def __init__(self, sys_argv):

        # Save all args provided without flags.
        self.all_args = [arg for arg in sys_argv if "--" not in arg]

        # Creating the command and other placeholder variables.
        self.command = None
        self.command_string = str()
        self.applicable_flags = list()

        # Analysing the flags.
        self.all_flags = [arg for arg in sys_argv if arg in ["--a", "--r", "--s", "--g", "--h", "--v"]]
        self.invalid_flags = [arg for arg in sys_argv if "--" in arg and arg not in self.all_flags]

        try:
            self.command_string = self.all_args[1]
            self.create_command()
            self.applicable_flags = list(set(self.all_flags) & set(self.command.available_flags))
            self.parameters = [arg for arg in sys_argv if
                               arg not in self.all_flags and arg not in [sys_argv[0],
                                                                         sys_argv[1]] and arg not in self.invalid_flags]
        except IndexError:
            # The blank seize command was run, no command, parameters or flags.
            pass

        # The final action is to finally assert whether or not this command is valid.
        self.isValid = True
        if not self.check_command() or not self.check_parameters() or not self.check_flags():
            self.isValid = False

    def create_command(self):
        # Create command
        if self.command_string == CommandStrings.THIS:
            command = This()
        elif self.command_string == CommandStrings.TRANSFER:
            command = Transfer()
        elif self.command_string == CommandStrings.SHIFT:
            command = Shift()
        else:
            command = Help()

        self.command = command

    @property
    def seize_script_path(self):

        if self.isValid:
            return self.all_args[0]

    @property
    def args(self):

        if self.isValid:
            return self.all_args[2::]

    def check_parameters(self):

        if "--h" not in self.all_flags:

            # Check to make sure each command has the correct number of arguments.
            if self.command_string == CommandStrings.THIS and len(self.parameters) != 1:
                print("This command requires one argument: the path to target directory. "
                      "Use 'seize help' for assistance.")
                return False
            elif self.command_string == CommandStrings.TRANSFER and len(self.parameters) != 2:
                print("This command requires two arguments: the path of the file to be moved and the path of the "
                      "directory to move the file to. Use 'seize help' for assistance.")
                return False
            elif self.command_string == CommandStrings.SHIFT and len(self.parameters) != 2:
                print("This command requires two arguments: the path of the directory to be moved and the path of the "
                      "directory to move the directory to. Use 'seize help' for assistance.")
                return False
            elif self.command_string == CommandStrings.HELP and len(self.parameters) != 0:
                print("This command requires zero arguments. Use 'seize help' for assistance.")
                return False

            # If not arguments are provided and the command is not 'help', take action.
            elif self.all_args[2::] == list() and self.command_string not in [CommandStrings.HELP, str()]:
                print("No arguments provided. Use 'seize help' for assistance.")
                return False

        return True

    def check_command(self):

        # If no command is given, welcome the user. This is however not valid in terms of creating a seize command.
        if len(self.all_args) == 1:
            print(
                Aesthetics.LOGO + "\nWelcome to the ultimate file migration tool. \nTime for you to seize the "
                                  "power of Seize. Use 'seize help' for assistance.")
            return False

        # If a command was given but it is not one of the available commands, take action.
        elif self.command_string not in [CommandStrings.THIS, CommandStrings.SHIFT, CommandStrings.TRANSFER,
                                         CommandStrings.HELP]:
            print("Command was not valid. Use 'seize help' for assistance.")
            return False

        return True

    def check_flags(self):

        # If invalid flags were present in the input, take action.
        if self.invalid_flags != list():
            print(f"Invalid flag(s): {self.invalid_flags}. Use 'seize help' for assistance.")
            return False

        # If help was requested, return false and print the relevant command's help message.
        if "--h" in self.all_flags:

            if self.command_string == CommandStrings.THIS:
                print(This().help)

            elif self.command_string == CommandStrings.SHIFT:
                print(Shift().help)

            elif self.command_string == CommandStrings.TRANSFER:
                print(Transfer().help)

            return False

        # Check for other flags, making sure they are valid for the command.
        else:
            if self.all_flags != self.applicable_flags:
                print("One or more flags provided are not applicable to this command.")
                return False

        return True
