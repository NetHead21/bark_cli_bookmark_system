from presentation.user_input import get_user_input


def get_new_bookmark_data() -> dict:
    return {
        "title": get_user_input("Title"),
        "url": get_user_input("URL"),
        "notes": get_user_input("Notes", required=False),
    }

def get_new_bookmark_info():
    bookmark_id = get_user_input("Enter a Bookmark ID to edit")
    field = get_user_input("Choose a value to edit (title, URL, notes)")
    new_value = get_user_input(f"Enter a new value for {field}")
    return {
        "id": bookmark_id,
        "update": {field: new_value}
    }


def get_bookmark_id_for_deletion() -> str:
    return get_user_input("Enter a bookmark ID to delete: ")


def get_github_import_options():
    return {
        "github_username": get_user_input("GitHub username"),
        "preserve_timestamps": get_user_input(
            "Preserve timestamps [Y/n]", required=False
        )
        in {"Y", "y", None},
    }
