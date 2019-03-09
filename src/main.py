from sys import argv

from src.command_checker import CommandChecker
from src.command_runner import CommandRunner


def seize():
    # Set up command handler
    command_handler = CommandChecker(sys_argv=argv)

    # Check if the entire command is valid
    if command_handler.is_valid:

        # Set up command runner
        command_runner = CommandRunner(command_handler.command,
                                       command_handler.parameters,
                                       command_handler.applicable_flags)

        # Run command in thread
        command_runner.start()
