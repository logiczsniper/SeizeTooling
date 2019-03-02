from src.constants import Commands, Aesthetics


class ArgumentHandler:

    def __init__(self, sys_argv):
        self.all_args = sys_argv
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
        if len(self.all_args) == 1:
            print(
                Aesthetics.LOGO + "\nWelcome to the ultimate file migration tool. \nTime for you to seize the "
                                  "power of Seize. Use --h for available commands and flags.\n\n")
            return False

        elif self.all_args[1] not in [Commands.THIS, Commands.SHIFT, Commands.TRANSFER]:
            raise ValueError("Command was not valid. Use --h for available commands and flags.")
        elif self.all_args[2::] == list():
            raise ValueError("No arguments provided. Use --h for available commands and flags.")
