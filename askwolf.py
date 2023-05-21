from backend.console_manager import manageconsole as mc
from backend.console_manager.menus import MunuPicker
from backend.connectwolf import WolfConnect
from backend.regiman import RegiMan
from resources import statics
from time import sleep
import sys

if __name__ == "__main__":
    regmanager = RegiMan(
        regpath=statics.RegVariables.HKEYPATH,
        appname=statics.RegVariables.APPNAME
    )
    applist = regmanager.enum_reg()
    regstatus = regmanager.check_regkey(
        apps=applist
    )
    while regstatus == True:
        appkey = regmanager.read_regkey()
        mc.clear_console()
        mainmenu = MunuPicker(title="Main Menu").show_mainmenu()
        menu_choice = input("Enter an option: ").strip()
        match menu_choice:
            case "1":
                query_input = input("Query: ")
                ask_simple = WolfConnect(
                    appid=appkey,
                    query=query_input
                )
                mc.space(1)
                print(f"Short Answer: {ask_simple.short_query()}")
                mc.space(1)
                print(f"Long Answer:\n{ask_simple.spoken_query()}")
                mc.space(1)
                simplecont_input = input(statics.SysResponses.CONT)
            case "2":
                comp_query = input("Query: ").strip()
                ask_comp = WolfConnect(
                    appid=appkey,
                    query=comp_query
                )
                mc.space(1)
                print(ask_comp.llm())
                mc.space(1)
                compcont_input = input(statics.SysResponses.CONT)
            case "3": sys.exit(
                statics.SysResponses.EXIT
            )
    else:
        while True:
            mc.clear_console()
            setup_input = input(
                statics.SetupResponses.QUESTION).upper().strip()
            match setup_input:
                case "Y":
                    print(statics.SetupResponses.WELCOME)
                    appid_input = input("Enter your APPID: ").strip()
                    regmanager.create_regkey(
                        appid=appid_input
                    )
                    print(statics.SetupResponses.APPID_SUCCESS)
                    sleep(5)
                    break
                case "N":
                    print(statics.SetupResponses.REGKEY_STATUS_ERROR)
                    sleep(5)
                    break
                case _:
                    print(statics.SetupResponses.INPUT_ERROR)
