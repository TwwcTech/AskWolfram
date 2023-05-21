from datetime import datetime


class API:
    SHORT_ANSWERS = "http://api.wolframalpha.com/v1/result?appid={}&i={}%3f"
    SPOKEN_RESULTS = "http://api.wolframalpha.com/v1/spoken?appid={}&i={}%3f"
    LLM = "https://www.wolframalpha.com/api/v1/llm-api?input={}&appid={}"


class SysVariables:
    DATETIME = f"{datetime.now().strftime(r'%d/%m/%Y %H:%M:%S')}"


class RegVariables:
    HKEYPATH = "Software\\"
    APPNAME = "AskWolfram"


class SysResponses:
    EXIT = "\nExiting the program, thank you for using 'askwolfram'\n"
    CONT = "Press 'Enter' to continue: "


class RegResponses:
    ENUM_ERROR = "Unable to enumerate regkeys: Please refer to the message above"
    CREATEKEY_ERROR = "Unable to create regkey: Please refer to the message above"
    READKEY_ERROR = "Unabel to read the key: Please refer to the message above"


class SetupResponses:
    INPUT_ERROR = "Not an option! Choose an option [Y/N]"
    REGKEY_STATUS_ERROR = "ERROR: Regkey does not exist, please check your regpath or start over!"
    WELCOME = "Welcome to 'askwolfram', where you can 'askwolfram' anything! :]\nStarting the setup script"
    QUESTION = "Regkey not found! Is this your first time running the program?: "
    APPID_SUCCESS = "APPID added! Please restart the program"
