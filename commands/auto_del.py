def auto_delete_message(config):
    text = f"AUTO DELETE MODE: {'ENABLED' if config['enabled'] else 'DISABLED'} ✅\nDELETE TIMER: {config['timer'] // 60} MINUTES ⏰"
    return text
