from pyrogram import Client, filters
from utils.command_handler import CommandHandler
from config import FORCE_SUB_CHANNELS

@filters.command("force_sub")
@CommandHandler.admin_only
async def force_sub_handler(client: Client, message):
    if not FORCE_SUB_CHANNELS:
        await message.reply("No force sub channels set.")
        return
    text = "Current Force Sub Channels:\n" + "\n".join(FORCE_SUB_CHANNELS)
    await message.reply(text)

@filters.command("req_force_sub_add")
@CommandHandler.admin_only
async def add_force_sub_handler(client: Client, message):
    if len(message.command) < 2:
        await message.reply("Please provide a channel username (e.g., /req_force_sub_add @channel)")
        return

    channel = message.command[1]
    if not channel.startswith("@"):
        channel = f"@{channel}"

    try:
        chat = await client.get_chat(channel)
        if chat.type not in ["channel", "supergroup"]:
            await message.reply("The provided chat is not a channel or supergroup!")
            return
        FORCE_SUB_CHANNELS.append(channel)
        await message.reply(f"Added {channel} to force sub channels.")
    except Exception as e:
        await message.reply(f"Error adding channel: {e}")

@filters.command("req_force_sub_remv")
@CommandHandler.admin_only
async def remove_force_sub_handler(client: Client, message):
    if len(message.command) < 2:
        await message.reply("Please provide a channel username (e.g., /req_force_sub_remv @channel)")
        return

    channel = message.command[1]
    if not channel.startswith("@"):
        channel = f"@{channel}"

    if channel in FORCE_SUB_CHANNELS:
        FORCE_SUB_CHANNELS.remove(channel)
        await message.reply(f"Removed {channel} from force sub channels.")
    else:
        await message.reply(f"Channel {channel} not found in force sub list.")
