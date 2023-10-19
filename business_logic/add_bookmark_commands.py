from datetime import datetime, timezone

from business_logic.create_bookmark_table_commands import db

from business_logic.command import Command


class AddBookmarkCommand(Command):
    def execute(self, data: dict, timestamp: object = None) -> tuple[bool, None]:
        data["date_added"] = timestamp or datetime.now(timezone.utc).isoformat()
        db.add("bookmarks", data)
        return True, None
