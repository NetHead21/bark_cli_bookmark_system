from persistence.database import DatabaseManager

from business_logic.command import Command

database: str = "bookmarks.db"
db: DatabaseManager = DatabaseManager(database)


class CreateBookmarksTableCommand(Command):
    def execute(self, data=None):
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
