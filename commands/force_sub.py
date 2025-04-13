def force_sub_list(channels: list):
    if not channels:
        return "No force sub channels set."
    return "Current Force Sub Channels:\n" + "\n".join(channels)
