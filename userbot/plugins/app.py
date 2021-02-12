"""Fetch App Details from Playstore.
.app <app_name> to fetch app details.
.appx <app_name> to fetch crack app """

import re
import bs4
import requests
from platform import uname
from telethon import events
from bs4 import BeautifulSoup
from telegraph import Telegraph
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import Var

from .. import CMD_HELP ,ALIVE_NAME
from ..utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"

@borg.on(admin_cmd(pattern=r"app (.*)"))
async def apk(event):
    app_name = event.pattern_match.group(1)
    event = await event.edit("Searching!")
    try:
        remove_space = app_name.split(' ')
        final_name = '+'.join(remove_space)
        page = requests.get("https://play.google.com/store/search?q="+final_name+"&c=apps")
        lnk = str(page.status_code)
        soup = bs4.BeautifulSoup(page.content,'lxml', from_encoding='utf-8')
        results = soup.findAll("div","ZmHEEd")
        app_name = results[0].findNext('div', 'Vpfmgd').findNext('div', 'WsMG1c nnK0zc').text
        app_dev = results[0].findNext('div', 'Vpfmgd').findNext('div', 'KoLSrc').text
        app_dev_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']
        app_rating = results[0].findNext('div', 'Vpfmgd').findNext('div', 'pf5lIe').find('div')['aria-label']
        app_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']
        app_icon = results[0].findNext('div', 'Vpfmgd').findNext('div', 'uzcko').img['data-src']
        app_details = "<a href='"+app_icon+"'>📲&#8203;</a>"
        app_details += " <b>"+app_name+"</b>"
        app_details += "\n\n<code>Developer :</code> <a href='"+app_dev_link+"'>"+app_dev+"</a>"
        app_details += "\n<code>Rating :</code> "+app_rating.replace("Rated ", "⭐ ").replace(" out of ", "/").replace(" stars", "", 1).replace(" stars", "⭐ ").replace("five", "5")
        app_details += "\n<code>Features :</code> <a href='"+app_link+"'>View in Play Store</a>"
        app_details += f"\n\n===> {DEFAULTUSER} <==="
        await event.edit(app_details, link_preview = True, parse_mode = 'HTML')
    except IndexError:
        await event.edit("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await event.edit("Exception Occured:- "+str(err))



@bot.on(admin_cmd(pattern="appx ?(.*)"))
async def mod(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()

CMD_HELP.update({
    "app":"__**PLUGIN NAME :** App__\
\n\n📌** CMD ➥** `.app` [app name]\
\nUSAGE   ➥  **Searches the app in the playstore and provides the link to the app in playstore and fetchs app details \
n\n📌** CMD ➥** `.appx` [app name]\
\nUSAGE   ➥  **Searches the hacked version of app nd send u \
"
})
