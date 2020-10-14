from pyrogram import Client
from pyrogram import filters
import time

app = Client(
    "my_account",
    api_id=1561405,
    api_hash="a38135e34dbecb5032d22d5739a6b967"
)

@app.on_message(filters.me & filters.command("info", prefixes="+"))
def inf(app, msg):
       nome = msg.reply_to_message.from_user.first_name
       username = msg.reply_to_message.from_user.username
       id = msg.reply_to_message.from_user.id
       dc = msg.reply_to_message.from_user.dc_id
       app.edit_message_text(msg.chat.id, msg.message_id, f"**ℹ️INFOℹ️**\n**♠️ NOME:** {nome}\n**🌄 Username: @{username}**\n**💻DC:  {dc}**\n**🆔 ID:** {id}")

@app.on_message(filters.me & filters.command("on", prefixes="+"))
def inf(app, msg):
       app.edit_message_text(msg.chat.id, msg.message_id, f"**ONLINE✅**")

@app.on_message(filters.me & filters.command("off", prefixes="+"))
def inf(app, msg):
       app.edit_message_text(msg.chat.id, msg.message_id, f"**OFFLINE🪐**")

@app.on_message(filters.me & filters.command("ban", prefixes="+"))
def inf(app, msg):
       nome = msg.reply_to_message.from_user.first_name
       app.edit_message_text(msg.chat.id, msg.message_id, f"**{nome} SEI STATO BANNATO DA ME♦️**")

  
@app.on_message(filters.me & filters.command("unban", prefixes="+"))
def inf(app, msg):
       nome = msg.reply_to_message.from_user.first_name
       app.edit_message_text(msg.chat.id, msg.message_id, f"**{nome} SEI STATO SBANNATO DA ME♦️**")  

@app.on_message(filters.me & filters.command("dev", prefixes="+"))
def inf(app, msg):
       app.edit_message_text(msg.chat.id, msg.message_id, f"**STO SVILUPPANDO  L'UBOT E QUINDI NON ROMPETEMI ADIOSSSSSS**")

@app.on_message(filters.me & filters.command("tornato", prefixes="+"))
def inf(app, msg):
       app.edit_message_text(msg.chat.id, msg.message_id, f"**SONO TORNATO BELLIIIIIIIII**")
@app.on_message(filters.me & filters.command("block", prefixes="+"))
def nome(client, message):
  app.edit_message_text(message.chat.id, message.message_id, f"**BLOCCATO L'EBREO✔🌚**")
  app.block_user(message.reply_to_message.from_user.id)

@app.on_message(filters.me & filters.command("unblock", prefixes="+"))
def nome(client, message):
  app.edit_message_text(message.chat.id, message.message_id, f"**SBLOCCATO L'EBREO✔🌚**")
  app.unblock_user(message.reply_to_message.from_user.id)

app.run()