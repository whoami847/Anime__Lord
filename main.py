from pyrogram import Client, idle, filters
from config import BOT_TOKEN, API_ID, API_HASH, LOG_LEVEL
import logging
import sys
import os
from aiohttp import web  # aiohttp ইমপোর্ট করা হলো
import asyncio

# logs/ ডিরেক্টরি তৈরি করা
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, "bot.log")),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Import handlers
from handlers.start_handler import start_handler
from handlers.help_handler import help_handler
from handlers.file_share_handler import file_share_handler
from handlers.batch_handler import batch_handler, batch_count_handler, batch_file_handler
from handlers.ban_handler import ban_handler, unban_handler
from handlers.auto_delete_handler import auto_delete_handler, toggle_auto_delete, set_timer, refresh_auto_delete, close_message
from handlers.force_sub_handler import force_sub_handler, add_force_sub_handler, remove_force_sub_handler
from handlers.broadcast_handler import broadcast_handler
from handlers.welcome_edit_handler import welcome_edit_handler, welcome_edit_img_handler
from handlers.about_edit_handler import about_edit_msg_handler, about_edit_img_handler
from handlers.settings_edit_handler import setting_edit_msg_handler, setting_edit_img_handler
from handlers.file_settings_handler import file_settings_handler, toggle_protect_content, toggle_hide_caption, toggle_channel_button, refresh_file_settings
from handlers.restart_handler import restart_handler

app = Client(
    "file_share_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register handlers
app.on_message(filters.command("start"))(start_handler)
app.on_message(filters.command("help"))(help_handler)
app.on_message(filters.command("genlink"))(file_share_handler)
app.on_message(filters.command("batch"))(batch_handler)
app.on_message(filters.regex(r"^\d+$"))(batch_count_handler)
app.on_message(filters.document)(batch_file_handler)
app.on_message(filters.command("ban"))(ban_handler)
app.on_message(filters.command("unban"))(unban_handler)
app.on_message(filters.command("auto_del"))(auto_delete_handler)
app.on_callback_query(filters.regex("toggle_auto_delete"))(toggle_auto_delete)
app.on_callback_query(filters.regex("set_timer"))(set_timer)
app.on_callback_query(filters.regex("refresh_auto_delete"))(refresh_auto_delete)
app.on_callback_query(filters.regex("close"))(close_message)
app.on_message(filters.command("force_sub"))(force_sub_handler)
app.on_message(filters.command("req_force_sub_add"))(add_force_sub_handler)
app.on_message(filters.command("req_force_sub_remv"))(remove_force_sub_handler)
app.on_message(filters.command("broadcast"))(broadcast_handler)
app.on_message(filters.command("welcome_edit"))(welcome_edit_handler)
app.on_message(filters.command("welcome_edit_img"))(welcome_edit_img_handler)
app.on_message(filters.command("about_edit_msg"))(about_edit_msg_handler)
app.on_message(filters.command("about_edit_img"))(about_edit_img_handler)
app.on_message(filters.command("setting_edit_msg"))(setting_edit_msg_handler)
app.on_message(filters.command("setting_edit_img"))(setting_edit_img_handler)
app.on_message(filters.command("files"))(file_settings_handler)
app.on_callback_query(filters.regex("toggle_protect_content"))(toggle_protect_content)
app.on_callback_query(filters.regex("toggle_hide_caption"))(toggle_hide_caption)
app.on_callback_query(filters.regex("toggle_channel_button"))(toggle_channel_button)
app.on_callback_query(filters.regex("refresh_file_settings"))(refresh_file_settings)
app.on_message(filters.command("restart"))(restart_handler)

# HTTP server for Koyeb health check
async def handle_health_check(request):
    return web.Response(text="Bot is running!", status=200)

async def start_http_server():
    http_app = web.Application()
    http_app.add_routes([web.get('/', handle_health_check)])
    runner = web.AppRunner(http_app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)  # পোর্ট ৮০৮০-এ সার্ভার চলবে
    await site.start()
    logger.info("HTTP server started on port 8080 for health check")

if __name__ == "__main__":
    logger.info("Starting File Share Bot...")
    try:
        # Pyrogram bot এবং HTTP সার্ভার একসাথে চালানোর জন্য asyncio ব্যবহার
        loop = asyncio.get_event_loop()
        loop.create_task(app.start())  # Pyrogram bot শুরু
        loop.create_task(start_http_server())  # HTTP সার্ভার শুরু
        loop.run_until_complete(idle())  # Bot চলতে থাকবে
        loop.run_until_complete(app.stop())  # Bot বন্ধ হলে স্টপ
    except Exception as e:
        logger.error(f"Bot crashed: {e}")
        raise
