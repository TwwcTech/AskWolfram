class API:
    SHORT_ANSWERS = "http://api.wolframalpha.com/v1/result?appid={}&i={}%3f"
    SPOKEN_RESULTS = "http://api.wolframalpha.com/v1/spoken?appid={}&i={}%3f"
    LLM = "https://www.wolframalpha.com/api/v1/llm-api?input={}&appid={}"


class WolframVariables:
    # TODO: create a reg_manager method and add appid to the regkey; read from there to access API
    APPID = "2HPKYW-33TYAJLGTY"


class SysResponses:
    EXIT = "\nExiting the program, thank you for using 'askwolfram'\n"
    CONT = "Press 'Enter' to continue: "
