import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot settings with environment variable fallback
BOT_TOKEN = os.getenv("BOT_TOKEN", "8162566389:AAFDO4ZLWCbrbIDZRxAFb2O9DBIVg1b9gYA")
API_ID = int(os.getenv("API_ID", "28774737"))
API_HASH = os.getenv("API_HASH", "851190ab85bb0b6dd547fff8e3c35b73")

# Database settings
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Anime:Anime@anime.suydbfe.mongodb.net/?retryWrites=true&w=majority&appName=Anime")
DB_NAME = os.getenv("DB_NAME", "Anime")

# Image directories with dynamic path resolution
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WELCOME_IMAGES_DIR = os.path.join(BASE_DIR, "images/welcome/")
ABOUT_IMAGES_DIR = os.path.join(BASE_DIR, "images/about/")
SETTINGS_IMAGES_DIR = os.path.join(BASE_DIR, "images/settings/")

# Default messages with multi-language support (future-ready)
WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE", "ʜᴇʏ, ɪ ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ғɪʟᴇ sʜᴀʀᴇ ʙᴏᴛ .")
ABOUT_MESSAGE = os.getenv("ABOUT_MESSAGE", "I am a private file sharing bot, meant to provide files and necessary stuff through special link for specific channels.")
SETTINGS_MESSAGE = os.getenv("SETTINGS_MESSAGE", "Here are the current settings of the bot.")

# Auto delete settings with customizable options
AUTO_DELETE_ENABLED = os.getenv("AUTO_DELETE_ENABLED", "True").lower() == "true"
AUTO_DELETE_TIMER = int(os.getenv("AUTO_DELETE_TIMER", "1200"))  # 20 minutes in seconds

# Force sub channels (list dynamically loaded from env)
FORCE_SUB_CHANNELS = os.getenv("FORCE_SUB_CHANNELS", "@just_test_only_0 , @log_chana").split(",") if os.getenv("FORCE_SUB_CHANNELS") else []

# Admins list loaded from environment variable
ADMINS = [int(admin_id) for admin_id in os.getenv("ADMINS", "7282066033").split(",")]

# Logging settings for advanced debugging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
