import sys

from business_logic.command import Command


class QuitCommand(Command):
    def execute(self, data=None) -> None:
        sys.exit()
