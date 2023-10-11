import os


def clear_screen() -> None:
    clear = "cls" if os.name == "nt" else "clear"
    os.system(clear)


def print_options(options: dict) -> None:
    for shortcut, option in options.items():
        print(f"({shortcut}) {option}")
    print()


def option_choice_is_valid(choice: str, options: dict) -> bool:
    return choice in options
