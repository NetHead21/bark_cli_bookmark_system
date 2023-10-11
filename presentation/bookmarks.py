from presentation.user_input import get_user_input


def get_new_bookmark_data() -> dict:
    return {
        "title": get_user_input("Title"),
        "url": get_user_input("URL"),
        "notes": get_user_input("Notes", required=False),
    }


def get_bookmark_id_for_deletion() -> str:
    return get_user_input("Enter a bookmark ID to delete: ")
