# Create by me @danish_00 😂😂
#
#  Anime wallpaper 😁😁
#
# HeHeHe
#
# Anime Plugins Modified By @Peroboyy
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="awall ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    reply_message = await event.get_reply_message()
    chat = "@NekosRobot"
    await event.edit("Searching ur anime wallpaper 😅😁...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1306903856))
              await event.client.send_message(chat, " /wallpaper")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @NekosRobot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

@borg.on(admin_cmd(pattern="awaifu ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    reply_message = await event.get_reply_message()
    chat = "@NekosRobot"
    await event.edit("Searching ur anime Anime Sticker For u 😅😁...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1306903856))
              await event.client.send_message(chat, " /waifu")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @NekosRobot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead bro now this cmd is useless 😂😂")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
