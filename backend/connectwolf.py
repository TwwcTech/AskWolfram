from resources.statics import API
import urllib.parse
import requests


class WolfConnect:
    def __init__(self, appid: str, query: str) -> None:
        self.query = query.strip()
        self.appid = appid.strip()

    def short_query(self):
        response = requests.get(
            url=API.SHORT_ANSWERS.format(
                self.appid,
                urllib.parse.quote_plus(self.query)
            )
        )
        return response.text

    def spoken_query(self):
        reponse = requests.get(
            url=API.SPOKEN_RESULTS.format(
                self.appid,
                urllib.parse.quote_plus(self.query)
            )
        )
        return reponse.text
