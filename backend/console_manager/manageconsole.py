import os as ops


def format_title(dashcount: int, titlename: str) -> str:
    dash = "-"
    return f"{dash*dashcount}{titlename}{dash*dashcount}"


def space(count: int): print("\n"*count)


def clear_console(): ops.system("cls") if ops.name == "nt" else ops.system("clear")
