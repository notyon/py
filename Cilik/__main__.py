# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# Cilik-PyroBot

from pyrogram import idle
from uvloop import install

from Cilik import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from Cilik.helpers.misc import create_botlog, git, heroku
from config import BOT_VER

MSG_ON = """
✅ **NandaPedia-Ubot Activated.**
**🏷️ Userbot Version -** `{}`
**Ketik** `.nandapedia` **untuk Mengecheck Bot**
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("nandapedia")
            await bot.join_chat("maestrocreation")
            await bot.join_chat("nandapediamember")
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER))
            except BaseException:
                pass
            LOGGER("NandaPedia").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("NandaPedia").info(f"NandaPedia-Ubot v{BOT_VER} ⚙️[⚡ Activated ⚡]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("NandaPedia").info("Starting NandaPedia-Ubot")
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
