import os
import re
import sys
import json
import time
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, PeerIdInvalid, UserIsBlocked, InputUserDeactivated
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Message
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,

# Features button
def register_feature_handlers(bot):
    @bot.on_callback_query(filters.regex("feat_command"))
    async def feature_button(client, callback_query):
        caption = "**✨ My Premium BOT Features :**"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📌 ᴀᴜᴛᴏ ᴘɪɴ ʙᴀᴛᴄʜ ɴᴀᴍᴇ", callback_data="pin_command")],
            [InlineKeyboardButton("💧 ᴡᴀᴛᴇʀᴍᴀʀᴋ", callback_data="watermark_command"), InlineKeyboardButton("🔄 ʀᴇsᴇᴛ", callback_data="reset_command")],
            [InlineKeyboardButton("🖨️ ʙᴏᴛ ᴡᴏʀᴋɪɴɢ ʟᴏɢs", callback_data="logs_command")],
            [InlineKeyboardButton("🖋️ ғɪʟᴇ ɴᴀᴍᴇ", callback_data="custom_command"), InlineKeyboardButton("🏷️ ᴛɪᴛʟᴇ", callback_data="titlle_command")],
            [InlineKeyboardButton("🎥 ʏᴏᴜᴛᴜʙᴇ", callback_data="yt_command")],
            [InlineKeyboardButton("🌐 ʜᴛᴍʟ", callback_data="html_command")],
            [InlineKeyboardButton("📝 ᴛᴇxᴛ ғɪʟᴇ", callback_data="txt_maker_command"), InlineKeyboardButton("📢 ʙʀᴏᴀᴅᴄᴀsᴛ", callback_data="broadcast_command")],
            [InlineKeyboardButton("🔙 ʙᴀᴄᴋ ᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ", callback_data="back_to_main_menu")]
        ])
        await callback_query.message.edit_media(
            InputMediaPhoto(
                media="https://files.catbox.moe/ixuknl.jpg",
                caption=caption
            ),
            reply_markup=keyboard
        )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
  
    @bot.on_callback_query(filters.regex("pin_command"))
    async def pin_button(client, callback_query):
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Feature", callback_data="feat_command")]])
        caption = f"**Auto Pin 📌 Batch Name :**\n\nAutomatically Pins the Batch Name in Channel or Group, If Starting from the First Link."
        await callback_query.message.edit_media(
            InputMediaPhoto(
                media="https://files.catbox.moe/ixuknl.jpg",
                caption=caption
            ),
            reply_markup=keyboard
        )

# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,

    @bot.on_callback_query(filters.regex("watermark_command"))
    async def watermark_button(client, callback_query):
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Feature", callback_data="feat_command")]])
      caption = f"**Custom Watermark :**\n\nSet Your Own Custom Watermark on Videos for Added Personalization."
      await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://files.catbox.moe/ixuknl.jpg",
          caption=caption
          ),
          reply_markup=keyboard
      )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("reset_command"))
    async def restart_button(client, callback_query):
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Feature", callback_data="feat_command")]])
      caption = f"**🔄 Reset Command:**\n\nIf You Want to Reset or Restart Your Bot, Simply Use Command /reset."
      await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://files.catbox.moe/ixuknl.jpg",
          caption=caption
          ),
          reply_markup=keyboard
      )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("logs_command"))
    async def pin_button(client, callback_query):
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Feature", callback_data="feat_command")]])
      caption = f"**🖨️ Bot Working Logs:**\n\n◆/logs - Bot Send Working Logs in .txt File."
      await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://files.catbox.moe/ixuknl.jpg",
          caption=caption
          ),
          reply_markup=keyboard
        )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("custom_command"))
    async def custom_button(client, callback_query):
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Feature", callback_data="feat_command")]])
      caption = f"**🖋️ Custom File Name:**\n\nSupport for Custom Name before the File Extension.\nAdd name ..when txt is uploading"
      await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://files.catbox.moe/ixuknl.jpg",
          caption=caption
          ),
          reply_markup=keyboard
      )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("titlle_command"))
    async def titlle_button(client, callback_query):
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Feature", callback_data="feat_command")]])
      caption = f"**Custom Title Feature :**\nAdd and customize titles at the starting\n**NOTE 📍 :** The Titile must enclosed within (Title), Best For appx's .txt file."
      await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://files.catbox.moe/ixuknl.jpg",
          caption=caption
          ),
          reply_markup=keyboard
      )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("broadcast_command"))
    async def pin_button(client, callback_query):
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Feature", callback_data="feat_command")]])
      caption = f"**📢 Broadcasting Support:**\n\n◆/broadcast - 📢 Broadcast to All Users.\n◆/broadusers - 👁️ To See All Broadcasting User"
      await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://files.catbox.moe/ixuknl.jpg",
          caption=caption
          ),
          reply_markup=keyboard
      )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("txt_maker_command"))
    async def editor_button(client, callback_query):
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Feature", callback_data="feat_command")]])
      caption = f"**🤖 Available Commands 🗓️**\n◆/t2t for text to .txt file\n"
      await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://files.catbox.moe/ixuknl.jpg",
          caption=caption
          ),
          reply_markup=keyboard
      )
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("yt_command"))
    async def y2t_button(client, callback_query):
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Feature", callback_data="feat_command")]])
      caption = f"**YouTube Commands:**\n\n◆/y2t - 🔪 YouTube Playlist → .txt Converter\n◆/ytm - 🎶 YouTube → .mp3 downloader\n\n<blockquote><b>◆YouTube → .mp3 downloader\n01. Send YouTube Playlist.txt file\n02. Send single or multiple YouTube links set\neg.\n`https://www.youtube.com/watch?v=xxxxxx\nhttps://www.youtube.com/watch?v=yyyyyy`</b></blockquote>"
      await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://envs.sh/GVi.jpg",
          caption=caption
          ),
          reply_markup=keyboard
      )

# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
    @bot.on_callback_query(filters.regex("html_command"))
    async def y2t_button(client, callback_query):
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Feature", callback_data="feat_command")]])
      caption = f"**HTML Commands:**\n\n◆/t2h - 🌐 .txt → .html Converter"
      await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://envs.sh/GVI.jpg",
          caption=caption
          ),
          reply_markup=keyboard
      )

# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
