from datetime import datetime, timezone

from business_logic.create_bookmark_table_commands import db


class AddBookmarkCommand:
    def execute(self, data: dict) -> str:
        data["date_added"] = datetime.now(timezone.utc).isoformat()
        db.add("bookmarks", data)
        return "Bookmark Added!"
