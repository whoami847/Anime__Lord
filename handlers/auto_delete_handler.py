from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.command_handler import CommandHandler
from config import AUTO_DELETE_ENABLED, AUTO_DELETE_TIMER
import json
import os

AUTO_DELETE_CONFIG_FILE = "database/auto_delete_config.json"

def load_auto_delete_config():
    if os.path.exists(AUTO_DELETE_CONFIG_FILE):
        with open(AUTO_DELETE_CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"enabled": AUTO_DELETE_ENABLED, "timer": AUTO_DELETE_TIMER}

def save_auto_delete_config(config):
    with open(AUTO_DELETE_CONFIG_FILE, "w") as f:
        json.dump(config, f)

async def auto_delete_handler(client: Client, message):
    config = load_auto_delete_config()
    text = f"AUTO DELETE MODE: {'ENABLED' if config['enabled'] else 'DISABLED'} ✅\nDELETE TIMER: {config['timer'] // 60} MINUTES ⏰"
    buttons = [
        [InlineKeyboardButton("DISABLE MODE" if config['enabled'] else "ENABLE MODE", callback_data="toggle_auto_delete")],
        [InlineKeyboardButton("SET TIMER", callback_data="set_timer")],
        [InlineKeyboardButton("REFRESH", callback_data="refresh_auto_delete")],
        [InlineKeyboardButton("CLOSE", callback_data="close")]
    ]
    await message.reply(
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

async def toggle_auto_delete(client: Client, callback_query):
    config = load_auto_delete_config()
    config["enabled"] = not config["enabled"]
    save_auto_delete_config(config)
    text = f"AUTO DELETE MODE: {'ENABLED' if config['enabled'] else 'DISABLED'} ✅\nDELETE TIMER: {config['timer'] // 60} MINUTES ⏰"
    buttons = [
        [InlineKeyboardButton("DISABLE MODE" if config['enabled'] else "ENABLE MODE", callback_data="toggle_auto_delete")],
        [InlineKeyboardButton("SET TIMER", callback_data="set_timer")],
        [InlineKeyboardButton("REFRESH", callback_data="refresh_auto_delete")],
        [InlineKeyboardButton("CLOSE", callback_data="close")]
    ]
    await callback_query.message.edit(
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

async def set_timer(client: Client, callback_query):
    await callback_query.message.reply("Please enter the new timer duration in minutes (e.g., 30):")

async def refresh_auto_delete(client: Client, callback_query):
    config = load_auto_delete_config()
    text = f"AUTO DELETE MODE: {'ENABLED' if config['enabled'] else 'DISABLED'} ✅\nDELETE TIMER: {config['timer'] // 60} MINUTES ⏰"
    buttons = [
        [InlineKeyboardButton("DISABLE MODE" if config['enabled'] else "ENABLE MODE", callback_data="toggle_auto_delete")],
        [InlineKeyboardButton("SET TIMER", callback_data="set_timer")],
        [InlineKeyboardButton("REFRESH", callback_data="refresh_auto_delete")],
        [InlineKeyboardButton("CLOSE", callback_data="close")]
    ]
    await callback_query.message.edit(
        text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

async def close_message(client: Client, callback_query):
    await callback_query.message.delete()
