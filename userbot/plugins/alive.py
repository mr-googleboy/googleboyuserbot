"""Check if userbot alive or not . """
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import CMD_HELP, ALIVE_NAME 
from userbot.utils import admin_cmd,sudo_cmd
from telethon import version
from platform import python_version, uname

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("░█─░█ █▀▀ █── █── █▀▀█\n"
                     "░█▀▀█ █▀▀ █── █── █──█\n"
                     "░█─░█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀\n\n" 
                     "☞Yes Sir ! I'm Alive\n"
                     f"`☞Telethon version: {version.__version__}\n`"
                     f"`☞Python: {python_version()}\n`"
                     f"☞Bot Creater : #Mr_Googleboy\n"
                     f"`☞My peru owner`: {DEFAULTUSER}\n\n"
                     "☞Join [Channel](https://t.me/feedbuzzme) For Latest Updates\n"
                     "[Deploy this super bot](https://github.com/mr-googleboy/googleboyuserbot)"
                    )
    
    


@borg.on(sudo_cmd(pattern="sudo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.reply("YOU ARE SUDO FOR THIS BOT \n\n"
                     f"☞Telethon version: {version.__version__}\n"
                     f"☞Python: {python_version()}\n"
                     f"☞My peru owner: {DEFAULTUSER}\n"
                     #"Deploy this userbot Now"
                    )
       
CMD_HELP.update({"alive": "`.alive` :\
      \nUSAGE: Type .alive to see wether your bot is working or not. "
}) 
