from sys import argv

from src.command_handler import CommandHandler


def seize():
    # Set up command handler
    command_handler = CommandHandler(sys_argv=argv)

    # Check if the entire command is valid
    if command_handler.is_valid:

        # Run command
        command_handler.command.run(command_handler.applicable_flags)
