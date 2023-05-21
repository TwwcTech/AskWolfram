from backend.console_manager import manageconsole as mc
from backend.console_manager.menus import MunuPicker
from backend.connectwolf import WolfConnect
from resources import statics
import sys

"""
# TODO: create a process to store the appid in the reg of the current user...
... making it (WAY) more secure than hardcoding it in the program, but also...
... makes it universal; anyone can use the program and not only it's author

# TODO: create a flow that checks for the appid; if the appid is found...
... read it, store it and use the appid for the appid perameter of the ...
... program; if the appid is not found, assume that its the first time...
... the program has ran and begin the setup process to continue
"""

if __name__ == "__main__":
    while True:
        mc.clear_console()
        mainmenu = MunuPicker(title="Main Menu").show_mainmenu()
        menu_choice = input("Enter an option: ").strip()
        match menu_choice:
            case "1":
                query_input = input("Query: ")
                ask_simple = WolfConnect(
                    appid=statics.WolframVariables.APPID,  # TODO: remove the hardcode
                    query=query_input
                )
                mc.space(1)
                print(f"Short Answer: {ask_simple.short_query()}")
                mc.space(1)
                print(f"Long Answer:\n{ask_simple.spoken_query()}")
                mc.space(1)
                simplecont_input = input(statics.SysResponses.CONT)
            case "2":
                comp_query = input(
                    "Comparative Query: [ex. 'What are the largest 3 countries?']: ").strip()
                ask_comp = WolfConnect(
                    appid=statics.WolframVariables.APPID,  # TODO: remove the hardcode
                    query=comp_query
                )
                mc.space(1)
                print(ask_comp.llm())
                mc.space(1)
                compcont_input = input(statics.SysResponses.CONT)
            case "3": sys.exit(
                statics.SysResponses.EXIT
            )
