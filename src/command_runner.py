from threading import Thread
from src.commands import Command
from typing import List


class CommandRunner(Thread):

    def __init__(self, command: Command, parameters: List, flags: List):
        super().__init__()
        self.flags = flags
        self.parameters = parameters
        self.command = command

    def run(self) -> None:
        self.command.run(self.parameters, self.flags)
