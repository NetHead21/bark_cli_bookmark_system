from business_logic.command import Command
from business_logic.create_bookmark_table_commands import db


class EditBookmarkCommand(Command):
    def execute(self, data) -> tuple[bool, None]:
        db.update(
            "bookmarks",
            {"id": data["id"]},
            data["update"],
        )
        return True, None
