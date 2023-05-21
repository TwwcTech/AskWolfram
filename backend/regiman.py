from resources.statics import SysVariables as sv
from resources.statics import RegResponses as rr
import winreg
import re


class RegiMan:
    def __init__(self, regpath: str, appname: str) -> None:
        self.regpath = regpath
        self.appname = appname
        self.c_datetime = sv.DATETIME
        self.access_reg = winreg.ConnectRegistry(
            None,
            winreg.HKEY_CURRENT_USER
        )
        self.access_regsoft = winreg.OpenKey(
            self.access_reg,
            "{}".format(
                self.regpath
            )
        )

    def enum_reg(self) -> list:
        try:
            appnames = []
            for softwarefolders in range(30):
                appnames.append(
                    winreg.EnumKey(
                        self.access_regsoft,
                        softwarefolders
                    )
                )
            return appnames
        except Exception as ex:
            raise Exception(
                ex,
                print(rr.ENUM_ERROR)
            )

    def check_regkey(self, apps: list) -> bool: return True if re.search(
        r"\b{}\b".format(
            self.appname
        ), str(apps)
    ) else False

    def create_regkey(self, appid: str):
        try:
            appname_key = winreg.CreateKey(
                self.access_regsoft,
                self.appname
            )
            winreg.SetValueEx(
                appname_key, "Init DateTime", 0,
                winreg.REG_SZ, self.c_datetime
            )
            winreg.SetValueEx(
                appname_key, "APPID", 0,
                winreg.REG_SZ, appid
            )
        except Exception as ex:
            raise Exception(
                ex,
                print(rr.CREATEKEY_ERROR)
            )

    def read_regkey(self) -> str:
        try:
            appname_key = winreg.OpenKey(
                self.access_regsoft,
                self.appname
            )
            appid = winreg.QueryValueEx(
                appname_key,
                "APPID"
            )
            id, index = appid
            return id
        except Exception as ex:
            raise Exception(
                ex,
                print(rr.READKEY_ERROR)
            )
