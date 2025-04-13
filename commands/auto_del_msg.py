def auto_delete_msg(new_message: str):
    with open("config.py", "r") as f:
        lines = f.readlines()

    with open("config.py", "w") as f:
        for line in lines:
            if line.startswith("AUTO_DELETE_MESSAGE"):
                f.write(f'AUTO_DELETE_MESSAGE = "{new_message}"\n')
            else:
                f.write(line)

    return f"Auto delete message updated to:\n{new_message}"
