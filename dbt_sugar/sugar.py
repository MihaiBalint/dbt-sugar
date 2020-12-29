#!/usr/bin/env python
"""
Orchestator module.

This module is in charge of executing the commands.
"""
import sys

from core.command.documentation import Documentation
from core.command.table import Table

COMMANDS = {"table": Table, "documentation": Documentation}


class Executor:
    """
    Executor class: Is in charge of executing the commands.

    Is the orchestator our commands.
    """

    VALID_ACTIONS = {c.get_command() for c in COMMANDS.values()}

    def help(self) -> None:
        # Method to display the help.
        for command in COMMANDS.values():
            command().help()
            print("")

    def __init__(self) -> None:
        command = sys.argv[1]
        if command == "help":
            self.help()
        elif command not in self.VALID_ACTIONS:
            print("The command is not valid. Please choose a valid command.")
            self.help()
        else:
            action = COMMANDS.get(command)
            action().main(sys.argv[2:])


if __name__ == "__main__":
    Executor()
