def add_force_sub(channel: str, channels: list):
    if channel in channels:
        return f"Channel {channel} is already in the force sub list."
    channels.append(channel)
    return f"Added {channel} to force sub channels."
