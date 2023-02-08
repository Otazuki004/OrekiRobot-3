import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import Button

from OrekiRobot import tbot as oreki
from OrekiRobot.events import register

POSTER = "https://t.me/OrekiMovies/7"

@register(pattern=("Thunivu"))
async def awake(event):
    CAP = """
Choose the size of Thunivu
"""

FIRST_BUTTON = [
        [
               InlineKeyboardButton(
               text="[247.7MB] SIZE FILE" url="https://telegram.me/OrekiProXBot?start=file1",
               text="[399.5MB] SIZE FILE" url="https://telegram.me/OrekiProXBot?start=file2",
               text="[700.3MB] SIZE FILE" url="https://telegram.me/OrekiProXBot?start=file3",
               text="[1.41GB] SIZE FILE" url="https://telegram.me/OrekiProXBot?start=file4",
            ),
       ]
  ]
 await oreki.send_file(event.chat_id, POSTER, caption=CAP, buttons=FIRST_BUTTON)

async def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]

async def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600 
    seconds %= 3600 
    minutes = seconds // 60 
    seconds %= 60 
    return "%d:%02d:%02d" % (hour, minutes, seconds)

async def awake(event):
 await event.reply("Uploading Please wait!")

file1 = "https://t.me/OrekiMovies/8"

async def awake(event):
    FILE_CAP = """
**Thunivu (2023) on HDRip 320p - x264 - Tamil - 250MB**
"""
 await oreki.send_file(event.chat_id, file1, caption=FILE_CAP)

file2 = "https://t.me/OrekiMovies/9"

async def awake(event):
    FILE2_CAP = """
**Thunivu (2023) on HDRip 480p - x264 - Tamil - 400MB**
"""
 await oreki.send_file(event.chat_id, file2, caption=FILE2_CAP)

file3 = "https://t.me/OrekiMovies/10"

async def awake(event):
    FILE3_CAP = """
**Thunivu (2023) on HDRip 720p - x264 - Tamil - 700MB**
"""
 await oreki.send_file(event.chat_id, file3, caption=FILE3_CAP)

file4 = "https://t.me/OrekiMovies/11"

async def awake(event):
    FILE4_CAP = """
**Thunivu (2023) on HDRip 1080p - x264 - Tamil - 1.5GB**
"""
 await oreki.send_file(event.chat_id, file4, caption=FILE4_CAP)

async def awake(event):
 await send.message("➠ Uploaded by : @OrekiProXBot!")

__mod_name__ = "Thunivu"