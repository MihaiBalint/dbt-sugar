"""
Table command.

TODO: Fill description.
"""
import argparse
from typing import List


class Table:
    """
    Table command.

    TODO: Fill description.
    """

    def generate_parser(self) -> None:
        # Method to generate the parser.
        self.parser = argparse.ArgumentParser(
            description="Command table helper.", usage=argparse.SUPPRESS
        )
        self.parser.add_argument("--table", "-t", required=True, help="Name of the table.")
        self.parser.add_argument(
            "--database",
            "-d",
            type=str,
            default="dwh",
            required=False,
            help="Database where the table is.",
        )

    def main(self, args: List[str]) -> None:
        """
        Main method.

        Args:
            args (List[str]): list of arguments that the user is using.
        """
        self.arg_parser = self.parser.parse_args(args)
        print("Creating table.")

    def help(self) -> None:
        # Print help from the parser.
        self.parser.print_help()

    def __init__(self) -> None:
        self.generate_parser()

    @staticmethod
    def get_command() -> str:
        """
        Method to get the command name.

        Returns:
            str: with the name of the command.
        """
        return "table"
