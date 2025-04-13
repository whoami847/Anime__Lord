def file_settings_message(config):
    text = (
        f"PROTECT CONTENT: {'ENABLED' if config['protect_content'] else 'DISABLED'} {'✅' if config['protect_content'] else '❌'}\n"
        f"HIDE CAPTION: {'ENABLED' if config['hide_caption'] else 'DISABLED'} {'✅' if config['hide_caption'] else '❌'}\n"
        f"CHANNEL BUTTON: {'ENABLED' if config['channel_button'] else 'DISABLED'} {'✅' if config['channel_button'] else '❌'}"
    )
    return text
