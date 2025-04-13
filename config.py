import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot settings with environment variable fallback
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")
API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash_here")

# Database settings
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "file_share_bot_v3")

# Image directories with dynamic path resolution
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WELCOME_IMAGES_DIR = os.path.join(BASE_DIR, "images/welcome/")
ABOUT_IMAGES_DIR = os.path.join(BASE_DIR, "images/about/")
SETTINGS_IMAGES_DIR = os.path.join(BASE_DIR, "images/settings/")

# Default messages with multi-language support (future-ready)
WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE", "ʜᴇʏ, ɪ ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ғɪʟᴇ sʜᴀʀᴇ ʙᴏᴛ ᴠ3.")
ABOUT_MESSAGE = os.getenv("ABOUT_MESSAGE", "I am a private file sharing bot, meant to provide files and necessary stuff through special link for specific channels.")
SETTINGS_MESSAGE = os.getenv("SETTINGS_MESSAGE", "Here are the current settings of the bot.")

# Auto delete settings with customizable options
AUTO_DELETE_ENABLED = os.getenv("AUTO_DELETE_ENABLED", "True").lower() == "true"
AUTO_DELETE_TIMER = int(os.getenv("AUTO_DELETE_TIMER", "1200"))  # 20 minutes in seconds

# Force sub channels (list dynamically loaded from env)
FORCE_SUB_CHANNELS = os.getenv("FORCE_SUB_CHANNELS", "").split(",") if os.getenv("FORCE_SUB_CHANNELS") else []

# Admins list loaded from environment variable
ADMINS = [int(admin_id) for admin_id in os.getenv("ADMINS", "123456789,987654321").split(",")]

# Logging settings for advanced debugging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
