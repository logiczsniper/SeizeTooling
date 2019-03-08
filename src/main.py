from sys import argv

from src.command_handler import CommandHandler


def seize():
    # Set up command handler
    command_handler = CommandHandler(sys_argv=argv)

    # Check if the entire command is valid - if not, return out of function.
    if not command_handler.is_valid:
        return None

    # Run command with the valid flags
    command_handler.command.run(command_handler.all_flags)
