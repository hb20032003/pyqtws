from config import QTWSConfig
from plugins import QTWSPlugin
from PyQt5.QtWebEngineWidgets import QWebEngineProfile


class ChangeUserAgent(QTWSPlugin):
    def __init__(self, user_agent: str):
        super().__init__("ChangeUserAgent")

        self.__default_user_agents = dict()
        self.__default_user_agents["chrome"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0"
        self.__default_user_agents["firefox"] = "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"

        if user_agent in self.__default_user_agents.keys():
            self.user_agent = self.__default_user_agents[user_agent]
        else:
            self.user_agent = user_agent

    def web_profile_setup(self, profile: QWebEngineProfile):
        profile.setHttpUserAgent(self.user_agent)


def instance(config: QTWSConfig, params: dict):
    return ChangeUserAgent(params["user-agent"].lower())
