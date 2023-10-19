import business_logic.add_bookmark_commands
import business_logic.create_bookmark_table_commands
import business_logic.delete_command
import business_logic.list_bookmarks_commands
import business_logic.quit_command
import business_logic.add_github_stars_commands
import business_logic.edit_bookmark_command
from collections import OrderedDict

from presentation.bookmarks import (
    get_new_bookmark_data,
    get_bookmark_id_for_deletion,
    get_github_import_options,
)
from presentation.options import Option
from presentation.user_input import get_option_choice
from presentation.utils import clear_screen, print_options

from presentation.bookmarks import get_new_bookmark_info


def loop():
    clear_screen()
    print("Welcome to Bark!")

    options = OrderedDict(
        {
            "A": Option(
                "Add a bookmark",
                business_logic.add_bookmark_commands.AddBookmarkCommand(),
                prep_call=get_new_bookmark_data,
                success_message="Bookmark added successfully!",
            ),
            "B": Option(
                "List bookmarks by date",
                business_logic.list_bookmarks_commands.ListBookmarksCommand(),
            ),
            "T": Option(
                "List bookmarks by title",
                business_logic.list_bookmarks_commands.ListBookmarksCommand(
                    order_by="title"
                ),
            ),
            "E": Option(
                "Edit a Bookmark",
                business_logic.edit_bookmark_command.EditBookmarkCommand(),
                prep_call = get_new_bookmark_info,
                success_message="Bookmark updated successfully!",
            ),
            "D": Option(
                "Delete a bookmark",
                business_logic.delete_command.DeleteBookmarkCommand(),
                prep_call=get_bookmark_id_for_deletion,
            ),
            "G": Option(
                "Import GitHub stars",
                business_logic.add_github_stars_commands.ImportGitHubStarsCommand(),
                prep_call=get_github_import_options,
                success_message = "Imported {result} bookmarks from starred repos!"
            ),
            "Q": Option("Quit", business_logic.quit_command.QuitCommand()),
        }
    )

    print_options(options)
    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()

    _ = input("Press ENTER to return to menu")


if __name__ == "__main__":
    business_logic.create_bookmark_table_commands.CreateBookmarksTableCommand().execute()
    while True:
        loop()
