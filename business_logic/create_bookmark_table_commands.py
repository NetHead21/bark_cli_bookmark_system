from persistence.database import DatabaseManager

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
