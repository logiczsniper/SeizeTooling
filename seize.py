from sys import argv
from src.argument_handler import ArgumentHandler


def main():
    # Set up arguments handler
    argument_handler = ArgumentHandler(sys_argv=argv)

    # Temp tests
    print("Args: " + str(argument_handler.args))
    print("Path: " + str(argument_handler.seize_script_path))
    print("Command: " + str(argument_handler.command))


if __name__ == "__main__":
    main()
