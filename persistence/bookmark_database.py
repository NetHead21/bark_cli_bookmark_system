from persistence import PersistenceLayer
from persistence.database import DatabaseManager


class BookmarkDatabase(PersistenceLayer):
    def __int__(self):
        self.table_name = "bookmarks"
        self.db = DatabaseManager("bookmarks.db")

        self.db.create_table(
            self.table_name,
            {
                "id": "integer primary key autoincrement",
                "title": "text not null",
                "url": "text not null",
                "notes": "text",
                "date_added": "text not null",
            },
        )

    def create(self, bookmark_data) -> None:
        self.db.add(self.table_name, bookmark_data)

    def list(self, order_by=None) -> object:
        return self.db.select(self.table_name, order_by=order_by).fetchall()

    def edit(self, bookmark_id, bookmark_data) -> None:
        self.db.update(self.table_name, {"id": bookmark_id}, bookmark_data)

    def delete(self, bookmark_id) -> None:
        self.db.delete(self.table_name, {"id": bookmark_id})
