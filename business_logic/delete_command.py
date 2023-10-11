from business_logic.create_bookmark_table_commands import db


class DeleteBookmarkCommand:
    def execute(self, data: dict) -> str:
        db.delete("bookmarks", {"id": data})
        return "Bookmak Deleted!"
