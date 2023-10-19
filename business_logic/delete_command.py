from business_logic.command import Command
from business_logic.create_bookmark_table_commands import db


class DeleteBookmarkCommand(Command):
    def execute(self, data: dict) -> tuple[bool, None]:
        db.delete("bookmarks", {"id": data})
        return True, None
