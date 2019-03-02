from constants import Commands


class ArgumentHandler:

    def __init__(self, sys_argv):
        self.all_args = sys_argv

        self.check_args()

    @property
    def seize_script_path(self):
        return self.all_args[0]

    @property
    def command(self):
        return self.all_args[1]

    @property
    def args(self):
        return self.all_args[2::]

    def check_args(self):
        if self.all_args[1] not in [Commands.THIS, Commands.SHIFT, Commands.TRANSFER]:
            raise (ValueError, "The command was not valid. \n\nUse --h for available commands and tags.")
