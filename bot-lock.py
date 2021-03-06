from pyrogram import Client , filters
from pyrogram.types import Message
#----------------------#
client = Client(
        session_name = "Robot" ,
        config_file = "config.ini"
)
open("lock.txt" , "w").write("")
#----------------------#
@client.on_message(filters.me)
async def all_message(_:client,m:Message):
    text = m.text

    if text == "/lockon":
        open("lock.txt" , "w").write("yes")
        await m.reply("با موفقیت قفل شد")
    elif text == "onlock":
        open("lock.txt" , "w").write("no")
        await m.reply("باز شد")
    #----------------------#

@client.on_message(filters.private)
async def all_message(_:client,m:Message):
    lock = open("lock.txt").read()
    lockon = True if lock == "yes" else False
    if lockon:
        await m.delete()
    else:
        m.continue_propagation()
#----------------------#
client.run()