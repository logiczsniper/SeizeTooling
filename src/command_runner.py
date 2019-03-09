from threading import Thread


class CommandRunner(Thread):

    def __init__(self, command, parameters, flags):
        super().__init__()
        self.flags = flags
        self.parameters = parameters
        self.command = command

    def run(self):
        self.command.run(self.parameters, self.flags)
