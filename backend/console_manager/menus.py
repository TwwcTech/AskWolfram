from backend.console_manager import manageconsole as mc


class MunuPicker():
    def __init__(self, title: str) -> None:
        self.menutitle = mc.format_title(
            dashcount=5,
            titlename=title.upper()
        )

    def show_mainmenu(self) -> str:
        menu_options = {
            "1": "Query",
            "2": "Detailed Query",
            "3": "Exit"
        }
        mc.space(1)
        print(self.menutitle)
        for options, menutype in menu_options.items():
            print(f"{options}-{menutype}")
        mc.space(1)
