from sys import argv
from src.argument_handler import ArgumentHandler
from src.constants import CommandStrings
from src.commands import *


def seize():
    # Set up arguments handler
    argument_handler = ArgumentHandler(sys_argv=argv)

    # Check if the args are valid - if not, return out of function.
    if not argument_handler.isValid:
        return None

    # Create command
    if argument_handler.command == CommandStrings.THIS:
        command = This()
    elif argument_handler.command == CommandStrings.TRANSFER:
        command = Transfer()
    else:
        command = Shift()

    print(argument_handler.flags)

    # Run command
    command.run()
