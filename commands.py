import sys
from datetime import datetime
from database import DatabaseManager
from datetime import timezone


database: str = "bookmarks.db"
db: DatabaseManager = DatabaseManager(database)


class CreateBookmarksTableCommand:
    def execute(self):
        db.create_table(
            "bookmarks",
            {
                "id": "integer primary key autoincrement",
                "title": "text not null",
                "url": "text not null",
                "notes": "text",
                "date_added": "text not null",
            },
        )


class AddBookmarkCommand:
    def execute(self, data: dict) -> str:
        data["date_added"] = datetime.now(timezone.utc).isoformat()
        db.add("bookmarks", data)
        return "Bookmark Added!"


class ListBookmarksCommand:
    def __init__(self, order_by: str = "date_added") -> None:
        self.order_by = order_by

    def execute(self):
        return db.select("bookmarks", order_by=self.order_by).fetchall()


class DeleteBookmarkCommand:
    def execute(self, data: dict) -> str:
        db.delete("bookmarks", {"id": data})
        return "Bookmak Deleted!"


class QuitCommand:
    def execute(self) -> None:
        sys.exit()
