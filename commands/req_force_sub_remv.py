def remove_force_sub(channel: str, channels: list):
    if channel not in channels:
        return f"Channel {channel} not found in force sub list."
    channels.remove(channel)
    return f"Removed {channel} from force sub channels."
