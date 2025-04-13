from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.command_handler import CommandHandler
import json
import os

FILE_SETTINGS_CONFIG_FILE = "database/file_settings_config.json"

def load_file_settings_config():
    if os.path.exists(FILE_SETTINGS_CONFIG_FILE):
        with open(FILE_SETTINGS_CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"protect_content": False, "hide_caption": True, "channel_button": True}

def save_file_settings_config(config):
    with open(FILE_SETTINGS_CONFIG_FILE, "w") as f:
        json.dump(config, f)

@filters.command("files")
@CommandHandler.admin_only
async def file_settings_handler(client: Client, message):
    config = load_file_settings_config()
    text = (
        f"PROTECT CONTENT: {'ENABLED' if config['protect_content'] else 'DISABLED'} {'✅' if config['protect_content'] else '❌'}\n"
        f"HIDE CAPTION: {'ENABLED' if config['hide_caption'] else 'DISABLED'} {'✅' if config['hide_caption'] else '❌'}\n"
        f"CHANNEL BUTTON: {'ENABLED' if config['channel_button'] else 'DISABLED'} {'✅' if config['channel_button'] else '❌'}"
    )
    buttons = [
        [InlineKeyboardButton("PROTECT CONTENT", callback_data="toggle_protect_content")],
        [InlineKeyboardButton("HIDE CAPTION", callback_data="toggle_hide_caption")],
        [InlineKeyboardButton("CHANNEL BUTTON", callback_data="toggle_channel_button")],
        [InlineKeyboardButton("SET BUTTON", callback_data="set_channel_button")],
        [InlineKeyboardButton("REFRESH", callback_data="refresh_file_settings")],
        [InlineKeyboardButton("CLOSE", callback_data="close")]
    ]
    await message.reply(
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@filters.callback_query(filters.regex("toggle_protect_content"))
async def toggle_protect_content(client: Client, callback_query):
    config = load_file_settings_config()
    config["protect_content"] = not config["protect_content"]
    save_file_settings_config(config)
    text = (
        f"PROTECT CONTENT: {'ENABLED' if config['protect_content'] else 'DISABLED'} {'✅' if config['protect_content'] else '❌'}\n"
        f"HIDE CAPTION: {'ENABLED' if config['hide_caption'] else 'DISABLED'} {'✅' if config['hide_caption'] else '❌'}\n"
        f"CHANNEL BUTTON: {'ENABLED' if config['channel_button'] else 'DISABLED'} {'✅' if config['channel_button'] else '❌'}"
    )
    buttons = [
        [InlineKeyboardButton("PROTECT CONTENT", callback_data="toggle_protect_content")],
        [InlineKeyboardButton("HIDE CAPTION", callback_data="toggle_hide_caption")],
        [InlineKeyboardButton("CHANNEL BUTTON", callback_data="toggle_channel_button")],
        [InlineKeyboardButton("SET BUTTON", callback_data="set_channel_button")],
        [InlineKeyboardButton("REFRESH", callback_data="refresh_file_settings")],
        [InlineKeyboardButton("CLOSE", callback_data="close")]
    ]
    await callback_query.message.edit(
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@filters.callback_query(filters.regex("toggle_hide_caption"))
async def toggle_hide_caption(client: Client, callback_query):
    config = load_file_settings_config()
    config["hide_caption"] = not config["hide_caption"]
    save_file_settings_config(config)
    text = (
        f"PROTECT CONTENT: {'ENABLED' if config['protect_content'] else 'DISABLED'} {'✅' if config['protect_content'] else '❌'}\n"
        f"HIDE CAPTION: {'ENABLED' if config['hide_caption'] else 'DISABLED'} {'✅' if config['hide_caption'] else '❌'}\n"
        f"CHANNEL BUTTON: {'ENABLED' if config['channel_button'] else 'DISABLED'} {'✅' if config['channel_button'] else '❌'}"
    )
    buttons = [
        [InlineKeyboardButton("PROTECT CONTENT", callback_data="toggle_protect_content")],
        [InlineKeyboardButton("HIDE CAPTION", callback_data="toggle_hide_caption")],
        [InlineKeyboardButton("CHANNEL BUTTON", callback_data="toggle_channel_button")],
        [InlineKeyboardButton("SET BUTTON", callback_data="set_channel_button")],
        [InlineKeyboardButton("REFRESH", callback_data="refresh_file_settings")],
        [InlineKeyboardButton("CLOSE", callback_data="close")]
    ]
    await callback_query.message.edit(
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@filters.callback_query(filters.regex("toggle_channel_button"))
async def toggle_channel_button(client: Client, callback_query):
    config = load_file_settings_config()
    config["channel_button"] = not config["channel_button"]
    save_file_settings_config(config)
    text = (
        f"PROTECT CONTENT: {'ENABLED' if config['protect_content'] else 'DISABLED'} {'✅' if config['protect_content'] else '❌'}\n"
        f"HIDE CAPTION: {'ENABLED' if config['hide_caption'] else 'DISABLED'} {'✅' if config['hide_caption'] else '❌'}\n"
        f"CHANNEL BUTTON: {'ENABLED' if config['channel_button'] else 'DISABLED'} {'✅' if config['channel_button'] else '❌'}"
    )
    buttons = [
        [InlineKeyboardButton("PROTECT CONTENT", callback_data="toggle_protect_content")],
        [InlineKeyboardButton("HIDE CAPTION", callback_data="toggle_hide_caption")],
        [InlineKeyboardButton("CHANNEL BUTTON", callback_data="toggle_channel_button")],
        [InlineKeyboardButton("SET BUTTON", callback_data="set_channel_button")],
        [InlineKeyboardButton("REFRESH", callback_data="refresh_file_settings")],
        [InlineKeyboardButton("CLOSE", callback_data="close")]
    ]
    await callback_query.message.edit(
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@filters.callback_query(filters.regex("refresh_file_settings"))
async def refresh_file_settings(client: Client, callback_query):
    config = load_file_settings_config()
    text = (
        f"PROTECT CONTENT: {'ENABLED' if config['protect_content'] else 'DISABLED'} {'✅' if config['protect_content'] else '❌'}\n"
        f"HIDE CAPTION: {'ENABLED' if config['hide_caption'] else 'DISABLED'} {'✅' if config['hide_caption'] else '❌'}\n"
        f"CHANNEL BUTTON: {'ENABLED' if config['channel_button'] else 'DISABLED'} {'✅' if config['channel_button'] else '❌'}"
    )
    buttons = [
        [InlineKeyboardButton("PROTECT CONTENT", callback_data="toggle_protect_content")],
        [InlineKeyboardButton("HIDE CAPTION", callback_data="toggle_hide_caption")],
        [InlineKeyboardButton("CHANNEL BUTTON", callback_data="toggle_channel_button")],
        [InlineKeyboardButton("SET BUTTON", callback_data="set_channel_button")],
        [InlineKeyboardButton("REFRESH", callback_data="refresh_file_settings")],
        [InlineKeyboardButton("CLOSE", callback_data="close")]
    ]
    await callback_query.message.edit(
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
  )
