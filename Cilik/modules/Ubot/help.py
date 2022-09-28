from prettytable import PrettyTable
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from Cilik import CMD_HELP
from Cilik.helpers.utility import split_list

heading = "──「 **{0}** 」──\n"

HELP_LOGO = "https://telegra.ph/file/8d9d5ec998234c4e43bca.jpg"


@Client.on_message(filters.command("help", [".", "-", "^", "!", "?"]) & filters.me)
async def module_help(client: Client, message: Message):
    cmd = message.command

    help_arg = ""
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        help_arg = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        all_commands = ""
        all_commands += "Please specify which module you want help for!! \nUsage: `.help [Nama Module]`\n\n"

        ac = PrettyTable()
        ac.header = False
        ac.title = "NandaPedia 𝗠𝗼𝗱𝘂𝗹𝗲𝘀"
        ac.align = "l"

        for x in split_list(sorted(CMD_HELP.keys()), 2):
            ac.add_row([x[0], x[1] if len(x) >= 2 else None])

        text = "NandaPedia 𝗠𝗼𝗱𝘂𝗹𝗲𝘀 \n\n"
        text += "♨ 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 : `[nanda]` - `[alive]` - `[heroku]`\n"
        text += "            `[system]` - `[update]`\n\n"
        text += "♣ 𝙏𝙤𝙤𝙡𝙠𝙞𝙩𝙨  : `[create]` - `[converter]` - `[gcast]`\n"
        text += "            `[info]` - `[invite]` - `[locks]`\n"
        text += "            `[profile]` - `[parse]` - `[paste]`\n"
        text += "            `[purge]` - `[sangmata]` - `[translate]`\n"
        text += "            `[vctools]`\n\n"
        text += "❣ 𝙁𝙪𝙣      : `[asupan]` - `[animasi]` - `[fakeaction]`\n"
        text += "             `[salam]` - `[toxic]` \n\n"
        text += "♞ 𝙊𝙩𝙝𝙚𝙧𝙨  : `[admins]` - `[afk]` - `[globals]`\n"
        text += "             `[groups]` - `[google]` - `[join]`\n"
        text += "             `[logs]` - `[misc]` - `[tulis]`\n"
        text += "             `[spam]` - `[sticker]` - `[sosmed]`\n"
        text += "             `[pmpermit]` - `[youtube]`\n\n"
        text += "👀 𝙋𝙧𝙚𝙛𝙞𝙭  : `[. - ^ ! ?]`\n"
        text += "          `  .help [Nama Module]`\n"

        await message.reply_photo(
            photo=HELP_LOGO,
            caption=text,
        )

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = "**❓ Help for Modules**\n\n"
            this_command += heading.format(str(help_arg)).upper()

            for x in commands:
                this_command += f"-⋟ `{str(x)}`\n```{str(commands[x])}```\n\n"

            await message.edit(this_command, parse_mode=enums.ParseMode.MARKDOWN)
        else:
            await message.edit(
                "`Please specify a valid module name.`",
                parse_mode=enums.ParseMode.MARKDOWN,
            )


def add_command_help(module_name, commands):

    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict
