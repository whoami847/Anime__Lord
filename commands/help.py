from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def help_message():
    text = (
        "I AM A PRIVATE FILE SHARING BOT, MEANT TO PROVIDE FILES AND NECESSARY STUFF THROUGH SPECIAL LINK FOR SPECIFIC CHANNELS.\n\n"
        "STILL HAVE DOUBTS, CONTACT BELOW PERSONS/GROUP AS PER YOUR NEED!"
    )
    buttons = [
        [InlineKeyboardButton("Support Chat Group", url="https://t.me/support_chat_group")],
        [InlineKeyboardButton("Owner", url="https://t.me/owner_username")],
        [InlineKeyboardButton("Developer", url="https://t.me/shidoteshika1")]
    ]
    return text, InlineKeyboardMarkup(buttons)
