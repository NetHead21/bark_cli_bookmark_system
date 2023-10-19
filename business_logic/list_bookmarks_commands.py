from business_logic.command import Command
from business_logic.create_bookmark_table_commands import db


class ListBookmarksCommand(Command):
    def __init__(self, order_by: str = "date_added") -> None:
        self.order_by = order_by

    def execute(self, data=None) -> tuple[bool, any]:
        return True, db.select("bookmarks", order_by=self.order_by).fetchall()
