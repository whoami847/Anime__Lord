def setting_edit_msg(new_message: str):
    with open("config.py", "r") as f:
        lines = f.readlines()

    with open("config.py", "w") as f:
        for line in lines:
            if line.startswith("SETTINGS_MESSAGE"):
                f.write(f'SETTINGS_MESSAGE = "{new_message}"\n')
            else:
                f.write(line)

    return f"Settings message updated to:\n{new_message}"
