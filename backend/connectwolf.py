from resources.statics import API
import urllib.parse
import requests


class WolfConnect:
    def __init__(self, appid: str, query: str) -> None:
        self.appid = appid.strip()
        self.query = urllib.parse.quote_plus(
            query.strip()
        )

    def short_query(self) -> str:
        response = requests.get(
            url=API.SHORT_ANSWERS.format(
                self.appid,
                self.query
            )
        )
        return response.text

    def spoken_query(self) -> str:
        reponse = requests.get(
            url=API.SPOKEN_RESULTS.format(
                self.appid,
                self.query
            )
        )
        return reponse.text

    def llm(self) -> str:
        response = requests.get(
            url=API.LLM.format(
                self.query,
                self.appid
            )
        )
        return response.text
