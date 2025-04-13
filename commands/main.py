from pyrogram import Client, idle
from config import BOT_TOKEN, API_ID, API_HASH, LOG_LEVEL
import logging
import sys

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/bot.log"),
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
app.on_message()(start_handler)
app.on_message()(help_handler)
app.on_message()(file_share_handler)
app.on_message()(batch_handler)
app.on_message()(batch_count_handler)
app.on_message()(batch_file_handler)
app.on_message()(ban_handler)
app.on_message()(unban_handler)
app.on_message()(auto_delete_handler)
app.on_callback_query()(toggle_auto_delete)
app.on_callback_query()(set_timer)
app.on_callback_query()(refresh_auto_delete)
app.on_callback_query()(close_message)
app.on_message()(force_sub_handler)
app.on_message()(add_force_sub_handler)
app.on_message()(remove_force_sub_handler)
app.on_message()(broadcast_handler)
app.on_message()(welcome_edit_handler)
app.on_message()(welcome_edit_img_handler)
app.on_message()(about_edit_msg_handler)
app.on_message()(about_edit_img_handler)
app.on_message()(setting_edit_msg_handler)
app.on_message()(setting_edit_img_handler)
app.on_message()(file_settings_handler)
app.on_callback_query()(toggle_protect_content)
app.on_callback_query()(toggle_hide_caption)
app.on_callback_query()(toggle_channel_button)
app.on_callback_query()(refresh_file_settings)
app.on_message()(restart_handler)

if __name__ == "__main__":
    logger.info("Starting File Share Bot...")
    try:
        app.run()
        idle()
    except Exception as e:
        logger.error(f"Bot crashed: {e}")
        raise
