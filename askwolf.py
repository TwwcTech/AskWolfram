from backend.console_manager import manageconsole as mc
from backend.console_manager.menus import MunuPicker
from backend.connectwolf import WolfConnect
from resources import statics
from time import sleep
import sys

if __name__ == "__main__":
    while True:
        mc.clear_console()
        mainmenu = MunuPicker(title1="Main Menu").show_mainmenu()
        menu_choice = input("Enter an option: ").strip()
        match menu_choice:
            case "1":
                query_input = input("Query: ")
                ask_simple = WolfConnect(
                    appid=statics.WolframVariables.APPID,
                    query=query_input
                )
                mc.space(1)
                print(f"Short Answer: {ask_simple.short_query()}")
                mc.space(1)
                print(f"Long Answer: {ask_simple.spoken_query()}")
                mc.space(1)
                break_input = input("Break? [Y/N]: ").upper().strip()
                match break_input:
                    case "Y": break
                    case "N": sleep(5)
                    case _: print("Not an option, please select [Y/N]")
            case "2":
                comp_query = input(
                    "Comparative Query: [ex. Whats the largest 3 US states?]: ").strip()
                ask_comp = WolfConnect(
                    appid=statics.WolframVariables.APPID,
                    query=comp_query
                )
                mc.space(1)
                print(f"Answer:\n{ask_comp.llm()}")
                mc.space(1)
                break
            case "3": sys.exit(
                "\nExiting the program, thank you for using 'askwolfram'\n"
            )
