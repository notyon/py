# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("c7c332a013d7d51359c763b3c2e1a9a3")
API_ID = int(getenv("API_ID", "25836327"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [
        -1001473548283,
        -1001687155877,
        -1001826062126,
    ]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "0.2.0@main"
BRANCH = "main"
CHANNEL = getenv("CHANNEL", "mengtawahhh")
DB_URL = getenv("DATABASE_URL", "mongodb+srv://ucik:ucik@cluster0.0l3r8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwXzQxMXI4dmFPUjBUQmxqMzFVeDNHSGFwcHg4eW5FbzJjZFA0Mw==").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "lpmcpf")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))

STRING_SESSION1 = getenv("STRING_SESSION1", "BAGKOycAe0z6I1TpVNH7lxZvks5SwBD5kG6wJ6OU2UdIO7J4s0uG2jpPuOeR8dImv-5ENRsk8J5RqT9UlqYvNsljBnivXZxAYHxx8dxef_j-AK_geuD8l1xEmXtN_WYpOXiqt5GY_CYrl9nub2j-a-Y0SJl2cpv6n__n5DlxvE8ArRYxLwa-j-hJUBOlh7OPQjdND6lB4-YCj-beFHMA89iocslDscuCpnKD-z31lREF6Z6WsYjWCia24IRp39SOydotnhb95glCUsOEiyU5OGQV34uyVCa2GPLymXLQJ9_d84w3f4MNnMHpvJVyGEIc3abpclOWHtZrpcUovbyeVfjosgdH1wAAAAHXC4ZhAQ")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
